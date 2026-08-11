# 异乡漫游客（Outland Wanderer）完整 Ren’Py 工程与简体中文翻译

本仓库包含从游戏 APK 整理出的完整 Ren’Py 工程，可在安装匹配版本的 Ren’Py SDK 后直接进行桌面运行、脚本检查和 Android 构建。

## 翻译包

- `game/tl/schinese/`：现有简体中文翻译，语言菜单中标为“旧版”。
- `game/tl/schinese_rewrite/`：根据开发者英文原文重译的新版，语言菜单中标为“重译”。新版保留 Ren’Py 变量、文本标签和菜单键，并覆盖开发者脚本中的对白、菜单及运行时静态字符串。

游戏内可从“设置 → 语言”切换两个简体中文语言包。

## 工程检查

完成翻译清单生成后，可用以下命令检查新版语言包的静态覆盖率：

```powershell
python tools/check_translation_coverage.py `
  --catalog _staging/developer-catalog.json `
  --package game/tl/schinese_rewrite `
  --report _staging/rewrite-coverage.json
```

检查器会报告缺失对白 ID、缺失菜单键、空译文、`pass`、重复项以及 Ren’Py 插值/标签不匹配。当前环境尚未安装 Ren’Py SDK，因此 APK 构建验证仍待 SDK 环境完成后执行。

## 游戏简介

平地起风波，你跌入了陌生的莫肯大陆。独在异乡为异客，在漫漫归乡路中，你会与这片土地的人们建立何种牵绊？你要如何应对冥冥之中的神秘力量？而你的命数又是几何？

## 官方相关链接

- [itch.io](https://f1shsticker.itch.io/outland-wanderer)
- [X](https://x.com/OutlandWanderer)
- [Discord](https://discord.gg/QnbJMGhZhV)
- [Patreon](https://www.patreon.com/OutlandWanderer)

## 非官方相关链接

- [游戏攻略](https://docs.google.com/document/d/1iVpfOl9_5MuRJGP1GADNVf63GPt6uRqxhLEVIJEneoI/edit?usp=sharing)
- [中文Telegram讨论群组](https://t.me/+YLrWVW2kEipmMjVl)

## 协作相关

本项目大体进度可至[里程碑](https://github.com/Outland-Wanderer/simplified-chinese/milestones)页面查询。

为了避免撞车和给各位译者提供更丰富的支持，若欲参与本项目，请先联系本项目负责人洽谈。

本项目章程详见[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## 研究资料

详见[CONTRIBUTING.md](CONTRIBUTING.md)

## 译者名单

- 逆戟鲸（[Telegram](https://t.me/COPtimer1974) | [X](https://x.com/COPtimer_1974)，项目负责人）
- Dcl5（[GitHub](https://github.com/1910857)）
- 机器熊猫（[邮箱](mailto:cx_zhang94@126.com)）
- LiamChace
