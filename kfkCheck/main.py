import os

#kafka 路径  topic名称  kafka地址端口
kfkdir = '/data/kafka/kafka01/'
topicname = 'quickstart-events04'
bootstrap = '133.0.124.212:39092'
command = r"%sbin/kafka-topics.sh --describe --topic %s --bootstrap-server %s | grep -v Configs | awk -F ' ' '{print $6}'" % (
    kfkdir, topicname, bootstrap)

# print(command)
commandres = os.popen(command)
res = commandres.read().rstrip('\n')



brokerlist = ''
with open('brokerid.txt', mode='r', encoding='utf8') as  f:
    brokerlist = f.read()

print(brokerlist)

for i in brokerlist:
    print(i)
# print(res)
