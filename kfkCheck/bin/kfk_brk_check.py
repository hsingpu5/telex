#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

ret = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.insert(0, ret)

from kfkCheck.bin.alter import alterinfo

debug = False
# debug=True
f = os.popen("hostname -i  ")
ip = f.read().strip('\n')
f.close()

# kafka 路径  topic名称  kafka地址端口(生产环境传参无效) zookeeper地址(生产使用 测试环境无效)
kfkdir = '/app/ofcs/kafka/kafka-server/'
topicname = 'plca_group_yc_lte3_topic_4'
bootstrap = '133.0.124.212:39092'
zookeeper = "133.0.208.212:2186,133.0.208.213:2186,133.0.208.214:2186"

brkid = {1, 2, 3, 4, 5, 6, }
# brkid = {1, 2, 3, 4, 5, 6, 7}  # debug
if not debug:
    command = (
                  "%sbin/kafka-topics.sh --describe "
                  "--topic %s --zookeeper %s | "
                  "grep -v Configs | awk -F ' ' '{print $10}' | sort |uniq"
              ) % (kfkdir, topicname, zookeeper)

else:
    command = (
                  "%sbin/kafka-topics.sh --describe "
                  "--topic %s --bootstrap-server %s | "
                  "grep -v Configs | awk -F ' ' '{print $10}' | sort |uniq"
              ) % (kfkdir, topicname, bootstrap)

print(command)
commandres = os.popen(command)
res = commandres.read().rstrip('\n')
brkset = set(res.replace('\n', ','))
brkset.discard(',')
# brkset={'6', '2', '5', '4', '3', '1'} #debugtest
print('在运行brkid:', brkset)


def brkgrep():
    for i in brkid:
        i = str(i)
        if i not in brkset:
            print(i, 'broker退服')
            return i


if __name__ == '__main__':
    downid = brkgrep()
    summary = 'kfk进程状态'
    description = str(ip + str(downid) + ': <--brokerID退服 | 策略中心 | 蔡俊南')
    # description = str('报警测试请忽略'+ip + str(downid)+': <--brokerID退服')
    print('退服列表:', downid)
    if downid:
        print('发送报警')
        res = alterinfo(ip, summary, description, paasServiceName='kfkgrp')
        print('发送状态', res)
