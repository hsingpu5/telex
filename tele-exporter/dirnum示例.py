#!/usr/bin/python3
from prometheus_client import start_http_server,Gauge
import os
import time
#定义数据类型，metric，describe(描述)，标签
dir_num = Gauge('dirNum','Calculate the number of directories',['instance'])

def get_dir_num():
  #获取目录个数
  path = "/root/"
  count = 0
  for cdir in os.listdir(path):
    if os.path.isdir(path+cdir) and not cdir.startswith('.'):
      count += 1
  #获取主机ip
  f = os.popen("hostname -i | awk '{print $2}'")
  ip = f.read().strip('\n')
  f.close()
  dir_num.labels(instance=ip).set(count)

if __name__ == "__main__":
 #暴露端口
  start_http_server(8000)
 #不断传入数据
  while True:
    get_dir_num()
    time.sleep(10)
