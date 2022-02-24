#!/usr/bin/env python3
from prometheus_client import start_http_server, Gauge
import os
import time

# 定义数据类型，metric，describe(描述)，标签

kfk_process = Gauge('kfk_process', '状态: kafka进程 ', ['instance'])


# kfk_process_num = Gauge('kfk_process', 'broker计数: Calculate the number of kafka processing num ', ['instance'])


def get_kfk_process():
    # 获取进程
    state = 0
    broker = os.popen("sudo ps -ef | grep kafkaBrokers |grep -v 'grep' | wc -l")

    broker.close()
    if broker:
        state = 1
    # 获取主机ip
    f = os.popen("hostname -i | awk '{print $2}'")
    ip = f.read().strip('\n')
    f.close()
    kfk_process.labels(instance=ip).set(state)


#    kfk_process_num.labels(instance=state).set(state)
#   kfk_process.labels(num=)
# kfk_process.labels(instance=ip).set()


if __name__ == "__main__":
    # 暴露端口
    start_http_server(8000)
    # 不断传入数据
    while True:
        get_kfk_process()
        time.sleep(1)
