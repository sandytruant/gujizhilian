# 插件安装方式

## 下载 RIME | 中州韵输入法 以及 librime-lua

RIME输入法是一款开源输入法，我们在其基础上开发插件。
我们的插件依赖于 librime-lua，librime-lua让我们能够利用lua脚本对RIME进行拓展。

### Windows

1. 从 https://rime.im/ 下载RIME输入法
2. 安装librime-lua，参考 https://github.com/hchunhui/librime-lua/wiki 下的 Installation 条目

### Linux

1. Linux下的RIME输入法需要运行在ibus或fcitx框架下，因此首先安装ibus/fcitx
2. 下载librime源代码：https://github.com/rime/librime
3. 下载librime-lua源代码：https://github.com/hchunhui/librime-lua
4. 编译并安装合并了librime-lua的librime：按照 https://github.com/hchunhui/librime-lua/wiki 中的Build条目
5. 安装RIME输入法（以fcitx5-rime为例）：https://github.com/fcitx/fcitx5-rime

## 安装古籍智联插件

1. 将此目录下的rime.lua以及luna_pinyin.custom.yaml复制到RIME的配置目录下（例如fcitx5-rime的配置目录是~/.local/share/fcitx5/rime）
2. 重新部署RIME/重启输入法后生效
