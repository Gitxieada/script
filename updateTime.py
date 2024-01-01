# -*- coding:utf-8 -*-
# 1.获取网络时间
# 2.修改系统时间
import http.client
import time
import os

def getTime(url):
     conn = http.client.HTTPConnection(url)
     conn.request("GET", "/")
     r = conn.getresponse()
     # r.getheaders() #获取所有的http头
     ts = r.getheader('date')  # 获取http头date部分
     # 将GMT时间转换成北京时间
     ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")  # 格式ts
     ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)  # +东八区
     dat = "date %u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
     tm = "time %02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
     return [dat, tm]


 #修改时间
def setTime(time):
    os.system(time[0])
    os.system(time[1])


if __name__ == "__main__":
    time_list = getTime('www.baidu.com')
    print(time_list)
    setTime(time_list)