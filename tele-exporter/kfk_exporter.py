#!/usr/bin/env python3
from prometheus_client import start_http_server, Gauge
import os
import time

# 定义数据类型，metric，describe(描述)，标签

kfk_process = Gauge('kfk_process', '状态: kafka进程是否存在 ', ['instance'])


def get_kfk_process():
    # 获取进程
    state = 0
    broker = os.popen("sudo ps -ef | grep kafkaBrokers |grep -v 'grep' | wc -l")

    if broker:
        state = 1
    broker.close()
    # 获取主机ip
    f = os.popen("hostname -i  ")
    ip = f.read().strip('\n')
    f.close()
    print('获取信息%s,%s' % (ip, state))
    kfk_process.labels(instance=ip).set(state)


if __name__ == "__main__":
    # 暴露端口
    start_http_server(9101)
    # 不断传入数据
    while True:
        get_kfk_process()
        time.sleep(1)
