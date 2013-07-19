#!/usr/bin/python
coding: UTF-8
import StringIO
import pycurl
import sys
import os
import json
class Test:
        def __init__(self):
                self.contents = ''
        def body_callback(self,buf):
                self.contents = self.contents + buf
 
def test_url(input_url):
        t = Test()
        #gzip_test = file("gzip_test.txt", 'w')
        c = pycurl.Curl()            #pycurl初始化
        c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
        c.setopt(pycurl.ENCODING, 'gzip')
        c.setopt(pycurl.URL,input_url)     
        c.perform()    #发送消息
        http_code = c.getinfo(pycurl.HTTP_CODE)         #HTTP 响应代码
        http_conn_time = c.getinfo(pycurl.CONNECT_TIME)   #远程服务器连接时间
        http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)   #连接上后到开始传输时的时间
        http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)  #接收到第一个字节的时间
        http_total_time = c.getinfo(pycurl.TOTAL_TIME)    #上一请求总的时间
        http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)       #下载的数据大小
        
        D = {"http_code":http_code,"http_size":http_size,"conn_time":http_conn_time,
        "pre_tran":http_pre_tran,"start_tran":http_start_tran,"total_time":http_total_time}
        
        for i in D.keys():
            print i,":",json.dumps(D[i])
 
if __name__ == '__main__':
        input_url = sys.argv[1]
        num = int(sys.argv[2])
        for i in range(num):
            print "第",i+1,"次监测："
            test_url(input_url)