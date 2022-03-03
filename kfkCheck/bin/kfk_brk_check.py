#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

ret = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(ret)
sys.path.insert(0, ret)
# print(sys.path)
#from kfkCheck.bin.alter import alterinfo

debug = False
# debug=True
f = os.popen("hostname -i  ")
ip = f.read().strip('\n')
f.close()

# kafka 路径  topic名称  kafka地址端口
kfkdir = '/app/ofcs/kafka/kafka-server/'
topicname = 'plca_group_yc_lte3_topic_4'
bootstrap = '133.0.124.212:39092'
zookeeper = "133.0.208.212:2186,133.0.208.213:2186,133.0.208.214:2186"
brkid={1,2,3,4,5,6}
brkid={1,2,3,4,5,6,7}  #debug
if not debug:
    command = r"%sbin/kafka-topics.sh --describe --topic %s --zookeeper %s | grep -v Configs | awk -F ' ' '{print $10}' | sort | uniq" % (
        kfkdir, topicname, zookeeper)
    print(command)
else:
    command = r"%sbin/kafka-topics.sh --describe --topic %s --bootstrap-server %s | grep -v Configs | awk -F ' ' '{print $6}'" % (
        kfkdir, topicname, bootstrap)
    print(command)
# print(command)
commandres = os.popen(command)
res = commandres.read().rstrip('\n')
brkset=set(res.replace('\n',','))
brkset.discard(',')
#brkset={'6', '2', '5', '4', '3', '1'} #debugtest
print ('在运行brkid:',brkset)
for i in brkid:
    i=str(i)
    if i not in brkset: 
        print(i,'broker退服')

# brokerlist = ''
# with open('brokerid.txt', mode='r', encoding='utf8') as  f:
#     brokerlist = f.read()
# print(brokerlist)
