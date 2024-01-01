# -*- coding: utf-8 -*-
import subprocess
import pyperclip
import os
import signal

def get_local_ip():
    import socket
    #获取到本机所有网卡的IP地址：
    IPs = socket.gethostbyname_ex(socket.gethostname())[-1]
    print(IPs)
    #想获取正在上网所使用的本机IP，通过route命令可以得到
    IP = [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]
    return IP

port = '5000'
 
# 获取当前文件所在目录的完整路径
current_dir = os.path.dirname(os.path.abspath(__file__))
print("当前文件所在目录的完整路径：", current_dir)

#当前目录下启动一个文件下载服务器
cmd='python -m http.server '+port

# 启动http.server
server_process = subprocess.Popen(['python', '-m', 'http.server',port], stdout=subprocess.PIPE,cwd=current_dir)
print("http.server is running. Process ID:", server_process.pid)
url=get_local_ip()+':'+port

#使用pyperclip模块的copy()把字符串拷贝到剪贴板
pyperclip.copy(url)

print("剪贴板已复制访问地址",pyperclip.paste())#打印剪贴板的内容

while True:
    Q = input("Enter q to quit!")
    if Q.lower() == 'q':
        # 关闭http.server
        os.kill(server_process.pid, signal.SIGTERM)
        print("http.server has been stopped.")
        break
    else:
        print("无效命令，请重新输入")




# Window 中杀死指定端口 cmd 命令行 taskkill
 # 1.查看指定端口5000的占用情况
# netstat -ano | findstr 5000
# 端口被进程号为4136的进程占用

# 2.直接强制杀死指定端口

# taskkill /pid 4136 -t -f


