#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys

ret = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(ret)
sys.path.insert(0, ret)
# print(sys.path)
from kfkCheck.bin.alter import alterinfo

f = os.popen("hostname -i  ")
ip = f.read().strip('\n')
f.close()


def get_kfk_state():
    state = 0
    # 获取进程
    broker = os.popen("/usr/java/jdk1.8.0_181/bin/jps | grep Kafka")
    res = broker.read().strip('\n')
    print('过滤结果:', res)
    if res:
        state = 1
    broker.close()
    print('IP地址:%s,进程状态:%s' % (ip, state))
    return state


if __name__ == '__main__':

    state = get_kfk_state()
    summary = 'kfk进程状态'
    description = str(ip + ':  KAFKA进程不存在 | 策略中心 | 蔡俊南')
    if not state:
        res = alterinfo(ip, summary, description, paasServiceName='kfkgrp')
        print('发送状态', res)
