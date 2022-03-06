brkset = {'4', '6', '1', '5', '2', '3'}
brkid = {1, 2, 3, 4, 5, 6, }

for i in brkid:
    i = str(i)
    if i in brkset:
        print(i, '在')
    else:
        print(i, '不在')

ip='1.1.1.1'
downid=2
summary = 'kfk进程状态'
description = str('策略中心kakfa集群异常,brokerID退服.|IP:%s,brokerID:%s.|蔡俊南' % (ip, str(downid)))
# description = str('报警测试请忽略'+ip + str(downid)+': <--brokerID退服')
print(description)