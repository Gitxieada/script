常用脚本：
1. http_server.py 简易的本地局域网脚本，类似于FTP下载的界面
2. updateTime.py 同步时间脚本

CMOS电池没电导致时间丢失，为了方便同步时间，写了一个脚本，可以把它放在启动项里，实现开机自动同步。

参考：
python windows时间同步工具 https://www.cnblogs.com/yunlongaimeng/p/10639006.html

Windows程序开机自启动（图文详解，命令快速打开目录） https://blog.csdn.net/MssGuo/article/details/114916265


打包成 exe 运行（方便在没有 Python 的电脑上使用）：
`pyinstaller -F -w updateTime.py -n 时间同步工具`

开机自启动:
- `win+r` 输入 `shell:startup`，打开用户自启动目录
- 创建`时间同步工具.exe` 的快捷方式，然后把快捷方式丢到win的自启目录下就可以。
