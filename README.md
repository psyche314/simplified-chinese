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

检查器会报告缺失对白 ID、缺失菜单键、空译文、`pass`、重复项以及 Ren’Py 插值/标签不匹配。Android APK 已在 Ren’Py 7.8.6、RAPT、JDK 21 和 Android SDK 环境中成功构建；桌面运行与真机运行尚未验证。

## 平台构建

Android、Windows、Linux 和 macOS 是四个并列的构建目标。这里要区分两个平台概念：`host` 是实际运行 Ren’Py SDK 命令行 Python 的系统，`target` 是要生成的游戏包的平台。`host` 和 `target` 不要求相同；例如，Windows host 可以生成 Linux 包或 macOS `.app` ZIP，Linux host 可以生成 Windows 包。

Android 使用 `android_build`，桌面平台使用 `distribute`。命令必须使用当前 host 对应的 SDK 内置 Python，不能因为 target 是其他系统而改用 target 的 Python。

### 选择 host 运行时

将 `RENPY_SDK` 设置为 SDK 目录后，按当前 host 选择对应的 `RENPY_PYTHON`：

| host | SDK 内置 Python |
| --- | --- |
| Windows | `%RENPY_SDK%\lib\py2-windows-x86_64\python.exe` |
| Linux | `$RENPY_SDK/lib/py2-linux-x86_64/python` |
| macOS | `$RENPY_SDK/lib/py2-mac-universal/python` |

Windows host：

```bat
set "RENPY_SDK=%USERPROFILE%\renpy-7.8.6-sdk"
set "RENPY_PYTHON=%RENPY_SDK%\lib\py2-windows-x86_64\python.exe"
```

Linux 或 macOS host：

```bash
export RENPY_SDK="$HOME/renpy-7.8.6-sdk"

# Linux host
export RENPY_PYTHON="$RENPY_SDK/lib/py2-linux-x86_64/python"

# macOS host（与上面的 Linux 设置二选一）
# export RENPY_PYTHON="$RENPY_SDK/lib/py2-mac-universal/python"
```

下面的 POSIX 示例假定已经设置了 `$RENPY_PYTHON`；Windows host 使用等价的 `%RENPY_PYTHON%` 写法。所有命令都应在项目根目录执行。

### Android target

Android 构建需要 Ren’Py 7.8.6 SDK、RAPT、JDK 21 和 Android SDK。它可以由支持的 Windows、Linux 或 macOS host 调用；host 只决定上表中的 Python 路径，`android_build` 决定 target。Gradle 缓存应保存在用户目录 `~/.gradle`，不应放入项目目录。

若要让编译出的 APK 包含 Live2D 动态头像，还必须把官方 [Live2D Cubism SDK for Native](https://www.live2d.com/en/sdk/download/native/) 安装到 Ren’Py SDK。当前工程与原版 APK 使用 Cubism 5 r.4.1：下载 `CubismSdkForNative-5-r.4.1.zip`，放到 `RENPY_SDK` 根目录，然后在 Ren’Py Launcher 的“Preferences → Install Live2D Cubism SDK for Native”中安装。Ren’Py 会把 Android 原生库安装到 SDK 的 RAPT prototype，构建时由 Gradle 正常打包；不安装时构建命令仍可能成功，但 APK 中不会有 Live2D Core，游戏会回退到占位表现。Live2D SDK 的下载和分发受 Live2D 许可证约束，请在官方页面阅读并接受相应协议。SDK 更新或重新安装 Android 支持后，需要重新安装 Live2D。

Linux/macOS host：

```bash
cd /path/to/outland-wanderer

export JAVA_HOME="/path/to/jdk-21"  # 按 host 的 JDK 安装路径调整
export GRADLE_USER_HOME="$HOME/.gradle"
export ANDROID_HOME="$HOME/Android/Sdk"
export ANDROID_SDK_ROOT="$ANDROID_HOME"

"$RENPY_PYTHON" \
  "$RENPY_SDK/renpy.py" \
  "$RENPY_SDK/launcher" \
  android_build . \
  --destination "$PWD/dist/android"
```

Windows host：

```bat
cd /d path\to\outland-wanderer

"%RENPY_PYTHON%" "%RENPY_SDK%\renpy.py" "%RENPY_SDK%\launcher" android_build . --destination "%CD%\dist\android"
```

构建完成后，APK 位于 `dist/android/`。RAPT 还会在 SDK 的 `rapt/bin/` 中保留一份内部产物，这是 Ren’Py 7.8.6 的默认行为。

### Windows target

`win` target 可从 Windows、Linux 或 macOS host 生成。

Linux/macOS host：

```bash
"$RENPY_PYTHON" \
  "$RENPY_SDK/renpy.py" \
  "$RENPY_SDK/launcher" \
  distribute . \
  --package win \
  --destination "$PWD/dist/windows"
```

Windows host：

```bat
"%RENPY_PYTHON%" "%RENPY_SDK%\renpy.py" "%RENPY_SDK%\launcher" distribute . --package win --destination "%CD%\dist\windows"
```

### Linux target

`linux` target 可从 Windows、Linux 或 macOS host 生成：

```bash
"$RENPY_PYTHON" \
  "$RENPY_SDK/renpy.py" \
  "$RENPY_SDK/launcher" \
  distribute . \
  --package linux \
  --destination "$PWD/dist/linux"
```

Windows host 使用：

```bat
"%RENPY_PYTHON%" "%RENPY_SDK%\renpy.py" "%RENPY_SDK%\launcher" distribute . --package linux --destination "%CD%\dist\linux"
```

输出为 `dist/linux/` 下的 Linux `.tar.bz2` 包。

### macOS target

macOS `.app` ZIP 可从 Windows、Linux 或 macOS host 生成。跨平台打包时显式指定 `app-zip`：

Linux/macOS host：

```bash
"$RENPY_PYTHON" \
  "$RENPY_SDK/renpy.py" \
  "$RENPY_SDK/launcher" \
  distribute . \
  --package mac \
  --format app-zip \
  --destination "$PWD/dist/macos"
```

Windows host：

```bat
"%RENPY_PYTHON%" "%RENPY_SDK%\renpy.py" "%RENPY_SDK%\launcher" distribute . --package mac --format app-zip --destination "%CD%\dist\macos"
```

DMG 依赖 macOS 的系统工具，只能在 macOS host 上生成：

```bash
"$RENPY_PYTHON" \
  "$RENPY_SDK/renpy.py" \
  "$RENPY_SDK/launcher" \
  distribute . \
  --package mac \
  --format app-dmg \
  --destination "$PWD/dist/macos"
```

代码签名和公证也必须在 macOS 上完成。Windows host 生成 Linux 或 macOS 包时，仍应在对应目标系统上进行启动、权限和发行流程验证。

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
