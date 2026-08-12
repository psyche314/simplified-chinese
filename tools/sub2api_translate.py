"""Send compact translation batches to a local OpenAI-compatible Responses API.

The driver deliberately does not edit Ren'Py files.  It joins a selected
catalog batch with the context audit, sends only source text plus relevant
context, and writes the complete response and a line-count-checked mapping to
an ignored staging directory.  A separate writer can then apply accepted
translations to the language package.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
import os
import re
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from translation_batches import escape_prompt_field


EMPTY_SOURCE_MARKER = "␀"
SPLIT_MARKER = "␟"
DEFAULT_ENDPOINT = "http://127.0.0.1:8080/v1/responses"
DEFAULT_MODEL = "gpt-5.6-luna"

PROJECT_GLOSSARY = (
    (
        "iron ores",
        "铁矿石",
        "iron ore 的复数；必须与 iron ingot（铁锭）区分。即使相邻游戏代码实际发放 Iron Ingot，也应按待翻译的开发者英文 source 译为“铁矿石”。",
    ),
    (
        "iron ore",
        "铁矿石",
        "未经冶炼的矿石；必须与 iron ingot（铁锭）区分。即使相邻游戏代码实际发放 Iron Ingot，也应按待翻译的开发者英文 source 译为“铁矿石”。",
    ),
    (
        "iron ingots",
        "铁锭",
        "iron ingot 的复数；已经冶炼成锭的材料，不要译成“铁矿石”。",
    ),
    (
        "iron ingot",
        "铁锭",
        "已经冶炼成锭的材料；不要译成“铁矿石”。",
    ),
    (
        "travelling carnival",
        "巡回嘉年华",
        "项目中的巡回综合嘉年华，会在平原上周期性扎营，设有帐篷、摊位和魔法秀；不要译成“旅行嘉年华”或“巡回马戏团”。",
    ),
    (
        "Travelling Carousal",
        "巡回嘉年华",
        "与 travelling carnival 指同一项巡回综合活动；不要另译成“巡回游艺会”或“巡回狂欢”。",
    ),
    (
        "Lusterfield",
        "卢斯特菲尔德",
        "村镇及其相关称号、地图和居民所属地的正式名称；不要按 lust 的普通含义改译。",
    ),
    (
        "Lusterfolk",
        "卢斯特菲尔德人",
        "卢斯特菲尔德的居民或派系成员；不要译成“长毛族”“露斯特族”或其他新种族名。",
    ),
    (
        "Lusterfolks",
        "卢斯特菲尔德人",
        "Lusterfolk 的复数写法；仍指卢斯特菲尔德的居民或派系成员。",
    ),
    (
        "Goat Tribe",
        "山羊部落",
        "与 Kechioeren 并列的派系名称；不要和地区名或人物名混用。",
    ),
    (
        "Kechioeren",
        "凯奇欧伦",
        "部族或地区专名；代码中的 scene、状态和变量标识符仍保持英文。",
    ),
    (
        "Nocturnal Trunk",
        "夜夜椿",
        "卢斯特菲尔德的酒馆/旅店名称；需要说明场所时可写“夜夜椿酒馆”。",
    ),
    (
        "King's Pawn",
        "君临典当",
        "卢斯特菲尔德的典当铺名称，不是国际象棋中的“国王的棋子”或“王兵”。",
    ),
    (
        "Sundersilk Cascades",
        "裂丝瀑布",
        "地图上的瀑布地点；不要译成“剪绸瀑布”或“丝绸瀑布”。",
    ),
    (
        "Sparkling Lagoon",
        "苍耀湖",
        "森林附近的湖泊地点名称。",
    ),
    (
        "Snowbound Summit",
        "雪封之巅",
        "雪地区域山峰及其相关地点名称；不要简化成“雪封山”。",
    ),
    (
        "Mokken",
        "莫肯",
        "大陆或地区名称；不要在书名、历史和地理语境中漏译。",
    ),
    (
        "Ardent Cauldron",
        "炽热坩埚",
        "山羊部落地区的商店/设施名称；不要改成“烈焰坩埚”。",
    ),
    (
        "Growth Potion",
        "成长药剂",
        "项目中的道具和配方名称；普通 growth 仍按句意译为生长、成长或长势。",
    ),
    (
        "Command Controller",
        "指令控制器",
        "项目中的道具和配方名称；不要译成“指挥控制器”或“命令控制器”。",
    ),
    (
        "Herb of Grace",
        "芸香",
        "项目中的草药道具名称；不要按字面译成“圣恩草”。",
    ),
    (
        "Horehound",
        "苦薄荷",
        "项目中的草药道具名称；不要误译成“夏枯草”或“欧夏至草”。",
    ),
    (
        "Horehounds",
        "苦薄荷",
        "Horehound 的复数写法；项目中的草药道具仍统一为“苦薄荷”。",
    ),
    (
        "Somni-Etern",
        "永恒梦魇",
        "药草志中的幻想蘑菇专名；大小写变化仍指同一种植物。该译名由药草志载体和专名语感决定，不代表所有西幻术语都应华丽意译。",
    ),
    (
        "Oolong Leaves",
        "乌龙茶叶",
        "雪山上的特殊植物道具；不要把植株、叶片和茶饮混成同一个词。",
    ),
    (
        "Oolong",
        "乌龙",
        "项目中的特殊植株/实体名称；普通饮品语境可根据 source 写成“乌龙茶”。",
    ),
    (
        "Surveying Bell",
        "测绘铃",
        "雪域墓室场景中的专属调查工具；代码状态 Detector 保持英文。",
    ),
    (
        "Primordial Runes",
        "原初符文",
        "项目中的符文名称；primordial 在其他短语中仍按语境处理。",
    ),
    (
        "Gruits",
        "格鲁伊特",
        "酿酒用的草药混合物，不是啤酒；普通 beer 仍译为啤酒。",
    ),
    (
        "Gruit",
        "格鲁伊特",
        "酿酒用的草药混合物，不是啤酒；普通 beer 仍译为啤酒。",
    ),
    (
        "Ribba's Ribald Magic Show",
        "里巴的荤趣魔法秀",
        "巡回嘉年华中的演出名称；保留成人喜剧语气，不改成泛称“魔术表演”。",
    ),
    (
        "Ribba",
        "里巴",
        "魔法师人物名；当前没有证据支持“瑞巴”作为有意别名。",
    ),
    (
        "Gwyddyon",
        "格威迪恩",
        "商人/供应商人物全名；只有 source 明确写 Gwyd 时才用短名“格威德”。",
    ),
    (
        "Gwyd",
        "格威德",
        "Gwyddyon 的明确短名；不要把全名也缩成“格威德”。",
    ),
    (
        "Ookko",
        "奥科",
        "原初实体/人物名；Axe of Ookko 应保持为“奥科之斧”。",
    ),
    (
        "Caretaker",
        "看守者",
        "雪山场景中的实体/战斗名称；不要与 Guardian 的“守护者”混同。",
    ),
    (
        "Spritebinder",
        "精灵缚者",
        "与八个幽灵实体相关的称谓；“八臂鬼”只能在 source 明确使用俗称时采用。",
    ),
    (
        "Eversprout",
        "永生芽",
        "项目中的植物/道具名称；Scroll of Eversprout 应译为“永生芽卷轴”。",
    ),
    (
        "Scroll of Eversprout",
        "永生芽卷轴",
        "项目中的卷轴道具名称。",
    ),
    (
        "Kantele",
        "坎特莱",
        "人物名的一部分；完整姓名为“坎特莱·科斯金”。",
    ),
    (
        "Kantele Koskin",
        "坎特莱·科斯金",
        "人物全名；不要在书名、演出署名和人物对白中漏掉姓氏或重新音译。",
    ),
    (
        "Eirik",
        "艾里克",
        "芬克尔之凝视的铁匠/制作者；人物名保持统一，不要改成其他音译。",
    ),
    (
        "Stigandr",
        "斯蒂甘德",
        "熊族历史中的征服者与先祖；不要保留英文或另造音译。",
    ),
    (
        "Bedwyr",
        "贝德维尔",
        "熊族旧任指挥官；不要把人物职务或姓名改成首领等其他称谓。",
    ),
    (
        "Chime",
        "齐门",
        "仅在上下文明确指向角色时译为“齐门”；句首大写不能单独证明是人名。铃铛、谜语、声音或号角语境中的 Chime/chime 应按句意译为“铃声”“鸣响”等。",
    ),
    (
        "Hezzong",
        "赫宗",
        "部落大长老的正式姓名；不要在叙述中保留英文。",
    ),
    (
        "Hezz",
        "赫宗",
        "Hezzong 的短称；只有源文明确使用 Hezz 时采用，代码标识符仍保持英文。",
    ),
    (
        "Pekoe",
        "佩克欧",
        "与精灵缚者传说相关的人物/名称；笔记和雕像铭文中保持同一音译。",
    ),
    (
        "Tevfik",
        "特夫菲克",
        "弗坎的父亲、山羊部落旧首领；不要在历史叙述和回忆场景中漂移为泰夫菲克或特维菲克。",
    ),
    (
        "Topu",
        "托普",
        "人物名；Topu's Gruit 应译为“托普的格鲁伊特”。",
    ),
    (
        "Topu's Gruit",
        "托普的格鲁伊特",
        "项目中的配方/道具名称，不是“托普的啤酒”或“托普的格鲁特酒”。",
    ),
    (
        "Axe of Ookko",
        "奥科之斧",
        "项目中的武器名称。",
    ),
    (
        "Cane",
        "凯恩",
        "酒馆老板人物名；这里不是普通名词 cane（手杖），也不要与 Cone 的假名混同。",
    ),
    (
        "Cone",
        "科恩",
        "剧情中故意使用的假名/误称；不要与人物真名 Cane 合并。",
    ),
    (
        "Kesi Alps",
        "凯西山脉",
        "莫肯北部山脉地点名；不要在矿石、凯奇欧伦和瀑布语境中改译为“凯西阿尔卑斯山”或其他名称。",
    ),
    (
        "Likkathia",
        "利卡希亚",
        "莫肯的王国/城镇名称；涉及国王、宫殿和利卡希亚铁盔时保持一致。",
    ),
    (
        "Likkathian",
        "利卡希亚",
        "Likkathia 的形容词形式；如 Likkathian Iron Helmet 仍使用“利卡希亚铁盔”。",
    ),
    (
        "Otsovaara",
        "奥措瓦拉",
        "熊族村落及其正式地名；不要在雪域剧情、历史和物品说明中漂移为“奥茨瓦拉”或“奥察瓦拉”。",
    ),
    (
        "Finnkel's Gaze",
        "芬克尔之凝视",
        "熊族地区的锻造铺/商店名称；不要沿用旧译“芬克尔深渊”，也不要在同一实体中混用“芬克尔之眼”。",
    ),
    (
        "Finnkel Abyss",
        "芬克尔深渊",
        "熊族所在的深渊地貌/地区名称；这是店名 Finnkel's Gaze 的地理来源，不要与店铺名称混为一谈。",
    ),
    (
        "Viscid Stream",
        "黏稠溪流",
        "黑暗森林与野生史莱姆区域之间的溪流地点名；不要与普通的黏液描述或“黏皮溪”混用。",
    ),
    (
        "Whispering Hollow",
        "低语空谷",
        "森林中的挖掘空地及任务区域名称；不要在地图、任务和剧情旁白中分别写成低语空洞、低语谷或低语幽谷。",
    ),
    (
        "Slime Country",
        "史莱姆之地",
        "北方史莱姆栖息区域名称；这里是地点，不是政治意义上的国家，避免使用史莱姆之国、史莱姆国度或史莱姆之乡。",
    ),
    (
        "Glaive Statue",
        "长戟雕像",
        "熊族墓穴中的敌方雕像名称；与 Bulwark Statue 并列出现，不要泛化为普通石像。",
    ),
    (
        "Bulwark Statue",
        "堡垒雕像",
        "熊族墓穴中的防御型敌方雕像名称；与 Glaive Statue 并列并负责防护/修复。",
    ),
    (
        "Stone Ward",
        "石之结界",
        "由 Rune Guardian 召唤的敌方实体名称；不要在战斗、逃跑和菜单文本中泛化成普通“石魔像”。",
    ),
    (
        "Rune Guardian",
        "符文守护者",
        "守护原初符文的敌方实体名称；不要与 Stone Ward 或普通 Guardian 混同。",
    ),
    (
        "Spriteling",
        "小精灵",
        "与 Spritebinder 相关的小型光谱敌方实体名称；不要译成泛称“幽魂”。",
    ),
    (
        "Methis",
        "梅西斯",
        "芬克尔之凝视的犀牛店主人物名；不要在同一角色中混用梅提斯、梅希斯或梅蒂斯。",
    ),
    (
        "Tetto",
        "泰托",
        "狼人剧情中的角色名；不要在战斗和剧情段落中混用“特托”。",
    ),
    (
        "feral werewolf",
        "狂化狼人",
        "因诅咒而陷入失控状态的狼人实体；战斗、任务、地图和剧情中统一使用“狂化狼人”。不要译成“野性狼人”“野蛮狼人”“野化狼人”或“野生狼人”；单独出现的 feral 仍按句法译为狂化、发狂或野性失控。",
    ),
    (
        "Kaurhu",
        "考尔胡",
        "熊族酋长人物名；Chief Kaurhu 可自然写成“考尔胡酋长”，但姓名本身保持不变。",
    ),
    (
        "Pirkka",
        "皮尔卡",
        "平原与酒馆中的吟游诗人人物名；不要因 bard、prose 或 lute 的上下文重新音译。",
    ),
    (
        "Wuldon",
        "伍尔顿",
        "狼人角色名；不要与旧译“沃尔登”混用。",
    ),
    (
        "Herd",
        "赫德",
        "熊族建造者人物名；源文中大写 Herd 才指该角色，普通小写 herd 仍按“兽群/群体”等上下文翻译。",
    ),
    (
        "Daggi",
        "达吉",
        "熊族指挥官人物名；Commander Daggi 可写成“达吉指挥官”，不要保留英文。",
    ),
    (
        "Tapjoo",
        "塔普乔",
        "山羊部落旧神人物名；不要在神殿、传说和历史文本中另造音译或意译。",
    ),
)

INSTRUCTIONS = """你是《Outland Wanderer》的简体中文本地化译者。你会收到一批按稳定 ID 定位的 Ren'Py 文本对象。每个对象的 source 字段就是开发者英语原文，也是本条事实的唯一来源；只翻译 source，其他字段只能用于理解和校验，绝不能把它们单独翻译或输出。

【执行优先级】
发生冲突时严格按以下顺序处理：
1. 输出协议与 Ren'Py 结构绝不能破坏。
2. 开发者英文 source 的人物、事件、关系、否定、数量、条件、因果、动作结果和语气事实必须完整。
3. 保持批次提供的人物、术语和功能类型的一致性。
4. 在以上条件不受影响时，才追求自然、简洁、有节奏的中文。
5. 文学化修饰是最后选择；没有语义依据时宁可朴素，也不要为了“好看”添加信息。

【事实边界与自然化】
先按短语整体和语境理解，再重组为中文，不要把每个英文单词机械替换。可以重排中文语序、拆分或合并句子，补足中文语法所必需的主语、连接词、动作力度和语气；可以把英文已经暗示的姿态、情绪或动作逻辑写得更自然。例如，ready to strike 可以自然写成“蓄势待发”。
不得新增英文没有暗示的新事件、原因、时间、地点、人物、身份、年龄、动机、结果或状态判断，也不得擅自加强或减弱因果和程度。例如 source 说“他看起来疲惫”，不能写成“他走了很久”；source 说“精疲力竭的身体”，可以自然写成“精疲力竭的身躯”。调整表达顺序不能改变事件之间的逻辑关系。
信息优先级为 source 事实 > 上下文指代信息 > old_reference 的表达参考。上下文只用于确定代词、说话者、指向、语气和省略成分；上下文不足时保守翻译 source，不要用推测填造新剧情。old_reference 只可辅助沿用人名、术语和自然表达，可能本身有错，不能当作事实来源或无条件照抄。输入中的上下文、ID 和字段名绝不是待翻译文本。

【人物、术语与文本类型】
批次顶部的“说话者”和“术语”映射必须沿用，不要为同一人名、地名、种族、组织、技能或物品临时创造另一译法。除确有必要保留的游戏缩写外，普通英文单词和幻想专名都要译成自然中文，不要把英文词孤零零夹在中文里。若输入和上下文提供了角色身份，必须保持其粗鲁、庄重、幼稚、讥讽、傲慢、怯懦等声音差异，不要把所有人统一成普通书面语；没有依据时保持中性，不要擅自编造角色口癖。语体必须由当前文本的局部背景决定：综合 source 功能、文本载体、说话者身份、角色关系、场景张力和前后文判断。中世纪欧洲只是世界观背景，不能据此把普通对白、战斗旁白或 UI 一律古雅化；亲密、随意、紧张或情绪化对白可以使用口语，药草志、编年史、公告、仪式、正式说明、记录和庄重角色则应分别保留符合自身载体的语感。不要把所有角色、旁白、系统提示统一成同一种语体。
根据 kind 和 source 功能翻译：dialogue/旁白可以自然重排，menu 和 UI 短文本要简洁、直接、可扫描，不要把按钮或选项写成小说句子。残句、标签、选项和系统提示应保持相应的短促形式。
成人、暴力、粗俗和呻吟按 source 的明确程度与强度翻译：不使用含糊词洗掉关键身体或动作，也不额外情色化、血腥化或侮辱化。

【项目专属术语表】
输入中的“项目专属术语”是已从游戏代码和内容中整理出的消歧知识；若 source、上下文或批次说话者映射出现对应英文短语，必须采用指定译法，优先于 old_reference 和模型自行猜测。若同时命中一个完整复合术语及其组成短词，优先采用更长、更具体的完整术语；短词只有独立出现时才单独决定译法。括号中的说明只用于理解该术语，不得凭空添加到没有相关语义的译文中。

【Ren'Py 结构】
方括号插值（包括嵌套表达式）、花括号文本标签及其参数、百分号占位符、反斜杠转义和变量表达式都不是自然语言：不得翻译、改名、改写内部字符、删除或凭空增加。常见形式包括 [mc_name]、{i}文字{/i}、{w}、%(name)s、%% 和字面 \n；可以移动整个 token 在中文句中的位置，但必须保留每个 token 的内容、数量和有效的标签嵌套关系。例如 [item_number] 不能写成 [ item_number]，{color=#ff0000} 与 {/color} 不能拆坏。中文与 token 之间是否留空格可以调整，但 token 内部一个字符也不能改变。
每个输入对象若有 protected_token_ledger，它是该 source 中所有受保护 token 的逐项清单，重复出现的 token 会在清单中重复列出。输出前先逐项核对清单；清单中的每一项都必须在译文中出现一次，不能合并、漏掉或凭空增加。这个清单是校验材料，不要输出或翻译它。
只有 source 字段严格等于空字符串 "" 时才输出 ␀；仅含空格、换行转义或其他控制字符的 source 仍然不是空源，按其原有结构处理，不得使用 ␀。kind=menu 的 source 必须保持为一个 new 字符串，source 内嵌换行要在同一输出行写成字面 \\n，不能使用 ␟；只有可拆分的 dialogue source 才能改写成多条相邻 Ren'Py 字符串。拆句只改变单行内部内容，不增加输出行数，绝对不要用物理换行拆句。

【高质量校准范例】
每个好例都同时优于坏例：事实更完整、中文更自然、语气更准确；不要把某个例子的修辞方式机械套用到其他文本。

英文：The golem instantly reacts to your advance, the moss on his surface vibrating profusely. His grip seems to have weakened as well.
坏例：魔像立刻对你的前进作出反应，表面的苔藓剧烈振动。他的握力似乎也减弱了。
好例：如此大胆的举动令石魔像立马起了反应，它身体表面的苔藓剧烈颤抖，握力似乎减弱了几分。
说明：好例重排了叙事并保留反应、苔藓和握力变化；坏例是生硬的逐词结构。

英文：You are facing a green slime, it is slowly slithering at you. You raise your fists, ready to strike at the gelatinous mass.
坏例：你正在面对一个绿色史莱姆，它正在慢慢向你蠕动。你抬起你的拳头，准备攻击这个胶状物质。
好例：史莱姆慢慢向你蠕动。你握紧双拳与这团粘液相视，铆足了劲。
说明：好例保留对峙、逼近和蓄力，并用中文动作顺序表达；坏例逐词翻译且节奏僵硬。

英文：You also found [gold_drop] gold and [exp_drop] EXP.
坏例：你还找到了金币和经验。
好例：你还找到[gold_drop]枚金币和[exp_drop]点经验。
说明：好例保留两个变量及其数量语义；变量内部必须逐字不变。

英文：Though, everyone's been talking about the alliance accord, so I might as well, strum {i}a chord{/i} on the lute.
坏例：大家都在谈论联盟协定，所以我不妨在鲁特琴上弹奏一曲。
好例：大家最近都在谈联盟协定，那我不妨在鲁特琴上弹奏{i}一曲{/i}。
说明：好例保留并正确包围斜体标签；标签内部不能被翻译或删除。

英文：Kari carries the furkan's exhausted body on his back. The two men grunts a little before walking.
坏例：卡里把弗坎疲惫的身体背在背上。两个男人在走路前发出一点咕哝声。
好例：卡里把精疲力竭的弗坎背在背上。两人轻轻哼了几声，才迈步离开。
说明：好例完整保留疲惫、背负、哼声和随后迈步；不得添加“说悄悄话”等新动作。

英文：Someone has to be the chief. I understand if I am not the best leader as my father.
坏例：有人必须是酋长。如果我不是像我父亲那样最好的领导者，我理解。
好例：总得有人来当酋长。我明白，自己不一定能像父亲那样成为出色的领袖。
说明：好例保留两句的事实和让步关系；不能为了顺口删掉后半句。

英文：The two immediately freeze. Their boners pointing at each other.
坏例：两人立刻僵住。他们的硬物正彼此相对。
好例：两人立刻僵住，彼此的肉棒正指向对方。
说明：好例保留成人场景的明确身体和方向；坏例含糊且不自然，不代表要额外增强尺度。

英文：I should be honest with you, Lothar. I was not there... when it happened.
坏例：我应该对你坦白，洛萨尔。事情发生的时候……我并不在场。
好例：我该跟你说实话，洛萨尔。事情发生的时候……我不在场。
说明：这里是亲密、情绪化的对白，所以“我该跟你说实话”比“我应该对你坦白”自然；这不是“对白一律口语化”的规则。语体必须根据人物、关系、场景和文本功能决定，正式说明或庄重角色仍应使用相应的书面表达。

英文：The Rune Guardian aims and flings 3 huge stones at you, it ignores your dodges and hit you right onto your body. Your health decreases by [ed] HP.
坏例：符石护卫瞄准你，掷来三块巨石。巨石无视你的闪避，正面砸中你的身体。你的生命值减少了[ed]点。
好例：符石护卫瞄准你，投来三块巨石。你试图闪躲，却仍被巨石正面砸中。你的生命值减少了[ed]点。
说明：好例用自然动作呈现“闪避仍然失败”，既不改成“来不及躲闪”，也不让巨石机械地“无视闪避”；普通战斗旁白中“投来”也比刻意偏书面的“掷来”更贴合语体。

【输出协议】
严格按输入对象顺序输出同样数量的行；每个对象恰好对应一行。每行只放该对象的纯中文译文，不输出编号、稳定 ID、引号、Ren'Py 代码、Markdown、项目符号、确认词、解释、表头、前后缀或空行。不要在行首或行尾添加空格。不要复述上下文；␟ 只能作为同一行内的拆句分隔符。
"""


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"无法读取 JSONL 第 {line_number} 行：{error}") from error
        if not isinstance(value, dict):
            raise ValueError(f"JSONL 第 {line_number} 行不是对象")
        records.append(value)
    return records


def compact(value: str | None) -> str:
    return escape_prompt_field(value) if value is not None else "-"


def _project_search_text(value: str) -> str:
    """Normalize punctuation used in English names without translating it."""

    value = value.replace("’", "'").replace("‘", "'")
    value = re.sub(r"\\[nrt]", " ", value)
    return re.sub(r"\s+", " ", value).strip().lower()


def _project_term_matches(source: str, term: str) -> bool:
    """Match a glossary entry as a phrase, not as an accidental substring."""

    normalized_source = _project_search_text(source)
    normalized_term = _project_search_text(term)
    pattern = rf"(?<![A-Za-z]){re.escape(normalized_term)}(?![A-Za-z])"
    if not re.search(pattern, normalized_source):
        return False
    # These entries are character-name disambiguators. Their lowercase forms
    # remain ordinary English words and must not activate the name glossary.
    if term in {"Cane", "Cone", "Herd", "Chime"}:
        return bool(re.search(rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])", source))
    return True


def build_prompt(records: list[dict[str, Any]], audits: dict[int, dict[str, Any]]) -> str:
    files = sorted({str(record["file"]) for record in records})
    scenes = sorted({str(audits[record["ordinal"]].get("scene_family", "")) for record in records})
    speaker_map = {}
    terms: dict[str, str] = {}
    register_notes: dict[str, str] = {}
    for record in records:
        audit = audits[record["ordinal"]]
        speaker = audit.get("speaker")
        if speaker:
            speaker_map[str(speaker)] = str(audit.get("speaker_name") or speaker)
        role = str(audit.get("text_role") or "未分类文本")
        note = str(audit.get("register_note") or "按 source 与前后文决定语体")
        register_notes[role] = note
        for term, references in (audit.get("term_references") or {}).items():
            if references:
                terms[str(term)] = str(references[0])

    searchable_context = "\n".join(
        str(record.get(field) or "")
        for record in records
        for field in ("source", "context_before", "context_after")
    )
    searchable_context += "\n" + "\n".join(speaker_map.values())
    project_terms = [
        f"{source}→{target}（{note}）"
        for source, target, note in PROJECT_GLOSSARY
        if _project_term_matches(searchable_context, source)
    ]
    project_terms.sort(key=len, reverse=True)

    lines = [
        "【批次上下文】",
        f"文件：{', '.join(files)}",
        f"场景类别：{', '.join(scene for scene in scenes if scene) or '未分类'}",
        "说话者：" + ("；".join(f"{alias}={name}" for alias, name in sorted(speaker_map.items())) or "无显式说话者"),
        "语体指南：" + "；".join(f"{role}={note}" for role, note in sorted(register_notes.items())),
        "术语：" + ("；".join(f"{source}→{target}" for source, target in sorted(terms.items())) or "无额外术语"),
        "项目专属术语：" + ("；".join(project_terms) or "本批次无"),
        "",
        "【输入格式】",
        f"下面每行是一个 JSON 对象。只翻译 source 字段；其它字段都是元数据或上下文，绝对不要把它们单独翻译或输出。context_before_only 和 context_after_only 是相邻原文，仅用于理解省略、指代和语气，不是额外的待翻译对象，也不增加输出行。JSON 中的 \\n 是字面转义，不是物理换行。输入对象总数固定为 {len(records)}：每个对象必须对应一行输出，包括 menu、很短的残句、很长的说明、重复 source 和带变量的 source；重复 source 也必须重复输出，不能合并或跳过。",
        "",
        f"【输入 JSONL，共 {len(records)} 个对象】",
    ]
    for record in records:
        audit = audits[record["ordinal"]]
        item = {
            "ordinal": record["ordinal"],
            "kind": record["kind"],
            "stable_id": record["id"],
            "speaker": audit.get("speaker"),
            "text_role": audit.get("text_role"),
            "source": record["source"],
            "old_reference": record.get("old_reference"),
            "required_context": audit.get("context_fields", []),
        }
        if audit.get("world_context"):
            item["world_context"] = audit["world_context"]
        protected_tokens: list[str] = []
        for opening, closing in (("[", "]"), ("{", "}")):
            tokens, _ = _balanced_tokens(record["source"], opening, closing)
            protected_tokens.extend(tokens)
        protected_tokens.extend(_PERCENT_TOKEN.findall(record["source"]))
        protected_tokens.extend(re.findall(r"\\(?:.|\Z)", record["source"], re.DOTALL))
        if protected_tokens:
            item["protected_token_ledger"] = protected_tokens
        if record.get("context_before") is not None:
            item["context_before_only"] = record["context_before"]
        if record.get("context_after") is not None:
            item["context_after_only"] = record["context_after"]
        lines.append(json.dumps(item, ensure_ascii=False, separators=(",", ":")))
    lines.extend(
        (
            "",
            "【输出】",
            f"按输入顺序只输出 {len(records)} 行纯译文。不要输出表头、编号或任何解释。",
        )
    )
    return "\n".join(lines)


def response_text(response: dict[str, Any]) -> str:
    pieces: list[str] = []
    for output in response.get("output", []):
        if not isinstance(output, dict):
            continue
        for content in output.get("content", []):
            if isinstance(content, dict) and content.get("type") == "output_text":
                text = content.get("text")
                if isinstance(text, str):
                    pieces.append(text)
    if not pieces:
        raise ValueError("Responses API 未返回 output_text")
    return "\n".join(pieces)


def _balanced_tokens(text: str, opening: str, closing: str) -> tuple[list[str], bool]:
    tokens: list[str] = []
    depth = 0
    start = -1
    escaped = False
    balanced = True
    for index, character in enumerate(text):
        if escaped:
            escaped = False
            continue
        if character == "\\":
            escaped = True
            continue
        if character == opening:
            if depth == 0:
                start = index
            depth += 1
        elif character == closing:
            if depth == 0:
                balanced = False
                continue
            depth -= 1
            if depth == 0:
                tokens.append(text[start : index + 1])
                start = -1
    if depth:
        balanced = False
    return tokens, balanced


_PERCENT_TOKEN = re.compile(
    r"(?<!\d)%(?:%|\([^)]*\)|[0-9]+\$)?[-+#0 ]*(?:[0-9]+|\*)?(?:\.[0-9]+|\.\*)?[hlL]?[A-Za-z]"
)
_ASCII_WORD = re.compile(r"(?<![A-Za-z])[A-Za-z]+(?![A-Za-z])")
_CHINESE_NUMERAL = re.compile(r"[零〇一二两三四五六七八九十百千万亿兆]")
# UI keys, stat abbreviations, version markers, proper names, and platform
# names that are intentionally preserved in otherwise Chinese text.
_ALLOWED_ASCII_TERMS = frozenset(
    {
        "A", "B", "C", "D", "E", "F", "H", "M", "O", "T", "W", "Y", "d", "f", "o", "v",
        "AGI", "Adobe", "CHA", "COPtimer", "Discord", "Dcl", "EXP", "Fábio",
        "Garamond", "HP", "INT", "LUST", "LonelyTree", "Magnolia", "MP",
        "Nyarlothotep", "Patreon", "Paul", "Pinewood", "PUR", "Pro", "RPG",
        "Ren", "Robotic", "Sannom", "STR", "TEN", "WASD", "Will", "Wisp",
        "XP", "Jerry", "Panda", "Py", "bio", "shsticker",
    }
)


def _protected_signature(text: str) -> dict[str, Any]:
    bracket_tokens, brackets_balanced = _balanced_tokens(text, "[", "]")
    tag_tokens, tags_balanced = _balanced_tokens(text, "{", "}")
    canonical_text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\\n")
    return {
        "brackets": Counter(bracket_tokens),
        "tags": Counter(tag_tokens),
        "percent_tokens": Counter(_PERCENT_TOKEN.findall(text)),
        "percent_count": text.count("%"),
        "escapes": Counter(re.findall(r"\\(?:.|\Z)", canonical_text, re.DOTALL)),
        "digits": Counter(re.findall(r"\d+(?:[.,]\d+)?", text)),
        "brackets_balanced": brackets_balanced,
        "tags_balanced": tags_balanced,
    }


def _unprotected_text(text: str) -> str:
    for opening, closing in (("[", "]"), ("{", "}")):
        tokens, _ = _balanced_tokens(text, opening, closing)
        for token in tokens:
            text = text.replace(token, " ")
    return re.sub(r"\\(?:.|\Z)", " ", text, flags=re.DOTALL)


def _protected_content_errors(
    source: str,
    translation: str,
    *,
    allow_paragraph_split: bool = False,
) -> list[str]:
    source_signature = _protected_signature(source)
    translation_signature = _protected_signature(translation)
    errors: list[str] = []
    if not translation_signature["brackets_balanced"]:
        errors.append("方括号不平衡")
    if not translation_signature["tags_balanced"]:
        errors.append("花括号文本标签不平衡")
    for label in ("brackets", "tags", "percent_tokens"):
        if source_signature[label] != translation_signature[label]:
            errors.append(
                f"{label}不一致：source={source_signature[label]!r}, "
                f"translation={translation_signature[label]!r}"
            )
    source_escapes = source_signature["escapes"]
    translation_escapes = translation_signature["escapes"]
    if allow_paragraph_split and SPLIT_MARKER in translation:
        source_escapes = source_escapes.copy()
        translation_escapes = translation_escapes.copy()
        source_escapes.pop(r"\n", None)
        translation_escapes.pop(r"\n", None)
    if source_escapes != translation_escapes:
        errors.append(
            f"escapes不一致：source={source_escapes!r}, "
            f"translation={translation_escapes!r}"
        )
    if source_signature["percent_count"] != translation_signature["percent_count"]:
        errors.append(
            "百分号数量不一致："
            f"source={source_signature['percent_count']}, "
            f"translation={translation_signature['percent_count']}"
        )
    if re.search(r"\d", source) and not re.search(r"\d", translation) and not _CHINESE_NUMERAL.search(translation):
        errors.append("源文本含数字，但译文没有阿拉伯数字或中文数字")
    source_unprotected = _unprotected_text(source)
    source_has_masked_fragment = bool(re.search(r"[-—]{2,}", source_unprotected))
    source_words = set(_ASCII_WORD.findall(source_unprotected))
    residual_words = [
        word
        for word in _ASCII_WORD.findall(_unprotected_text(translation))
        if word not in _ALLOWED_ASCII_TERMS
        and not (source_has_masked_fragment and word in source_words)
    ]
    if residual_words:
        errors.append(f"疑似未翻译的拉丁词：{residual_words!r}")
    return errors


def validate_lines(text: str, records: list[dict[str, Any]]) -> list[str]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    while lines and not lines[-1].strip():
        lines.pop()
    if len(lines) != len(records):
        raise ValueError(f"译文行数为 {len(lines)}，输入条数为 {len(records)}")

    validated: list[str] = []
    errors: list[str] = []
    for index, (line, record) in enumerate(zip(lines, records), 1):
        if not line.strip():
            errors.append(f"第 {index} 条译文为空：ordinal={record['ordinal']}")
            continue
        if "\t" in line or line.startswith("```"):
            errors.append(f"第 {index} 条译文包含未允许的格式：{line!r}")
            continue
        if record.get("source") == "":
            if line != EMPTY_SOURCE_MARKER:
                errors.append(f"第 {index} 条空源文本必须输出 {EMPTY_SOURCE_MARKER!r}")
        elif line == EMPTY_SOURCE_MARKER:
            errors.append(f"第 {index} 条非空源文本错误地输出空源标记")
        if any(not part.strip() for part in line.split(SPLIT_MARKER)):
            errors.append(f"第 {index} 条拆句译文包含空分段：ordinal={record['ordinal']}")
        if record.get("kind") == "menu" and SPLIT_MARKER in line:
            errors.append(f"第 {index} 条 menu 不能用 {SPLIT_MARKER} 拆成多段：ordinal={record['ordinal']}")
        if record.get("source") and line != EMPTY_SOURCE_MARKER:
            errors.extend(
                f"第 {index} 条 ordinal={record['ordinal']}：{error}"
                for error in _protected_content_errors(
                    record["source"],
                    line,
                    allow_paragraph_split=record.get("kind") == "dialogue",
                )
            )
        validated.append(line.strip())
    if errors:
        raise ValueError("翻译协议校验失败：\n" + "\n".join(errors))
    return validated


def request_response(endpoint: str, api_key: str, model: str, prompt: str, max_output_tokens: int, effort: str) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "instructions": INSTRUCTIONS,
        "input": prompt,
        "max_output_tokens": max_output_tokens,
        "store": False,
    }
    if effort != "default":
        payload["reasoning"] = {"effort": effort}
    request = Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=1800) as response:
            body = response.read()
    except HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Responses API HTTP {error.code}: {details}") from error
    except URLError as error:
        raise RuntimeError(f"无法连接 Responses API：{error}") from error
    try:
        value = json.loads(body.decode("utf-8"))
    except json.JSONDecodeError as error:
        raise RuntimeError("Responses API 返回的不是 JSON") from error
    if not isinstance(value, dict):
        raise RuntimeError("Responses API 返回的 JSON 不是对象")
    if value.get("error"):
        raise RuntimeError(f"Responses API 返回错误：{value['error']}")
    return value


def translate_command(args: argparse.Namespace) -> int:
    records = read_jsonl(args.records)
    audit_records = read_jsonl(args.context_audit)
    audits = {int(record["ordinal"]): record for record in audit_records}
    missing = [record["ordinal"] for record in records if int(record["ordinal"]) not in audits]
    if missing:
        raise ValueError(f"context audit 缺少 ordinal：{missing}")
    if not records:
        raise ValueError("翻译批次为空")

    api_key = args.api_key or os.environ.get("OUTLAND_SUB2API_API_KEY")
    if not api_key:
        raise ValueError("请通过 --api-key 或 OUTLAND_SUB2API_API_KEY 提供本地 API key")

    args.output.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(records, audits)
    (args.output / "request.prompt.txt").write_text(prompt, encoding="utf-8", newline="\n")
    response = request_response(args.endpoint, api_key, args.model, prompt, args.max_output_tokens, args.reasoning_effort)
    (args.output / "response.json").write_text(
        json.dumps(response, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    text = response_text(response)
    (args.output / "output.raw.txt").write_text(text, encoding="utf-8", newline="\n")
    translations = validate_lines(text, records)
    with (args.output / "translations.tsv").open("w", encoding="utf-8", newline="\n") as handle:
        for record, translation in zip(records, translations):
            handle.write(f"{record['ordinal']}\t{translation}\n")
    usage = response.get("usage") if isinstance(response.get("usage"), dict) else {}
    metadata = {
        "records": len(records),
        "model": args.model,
        "endpoint": args.endpoint,
        "reasoning_effort": args.reasoning_effort,
        "output_lines": len(translations),
        "usage": usage,
        "status": response.get("status"),
    }
    (args.output / "result.meta.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(metadata, ensure_ascii=False))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--records", type=Path, required=True, help="选定批次的 Record JSONL")
    parser.add_argument("--context-audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--api-key")
    parser.add_argument("--max-output-tokens", type=int, default=16000)
    parser.add_argument("--reasoning-effort", choices=("default", "low", "medium", "high"), default="medium")
    parser.set_defaults(function=translate_command)
    return parser


if __name__ == "__main__":
    try:
        arguments = build_parser().parse_args()
        raise SystemExit(arguments.function(arguments))
    except (RuntimeError, ValueError) as error:
        print(f"错误：{error}", file=sys.stderr)
        raise SystemExit(1)
