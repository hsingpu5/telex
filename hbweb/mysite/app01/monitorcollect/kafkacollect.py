# zookeeper monitor information

import requests, time

# from app01.views import checktime
checktime = str(time.time())[0:14]
import json


def kfk_clsname():
    clsname = []
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('kafka_brokers', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')

        for e in res:
            clsname.append(e.get('metric').get('cluster'))
    return clsname


def kfkgather(cluster):
    zk_dic = {}
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('kafka_brokers', checktime,)
    res = requests.get(url)
    if res.status_code == 200:
        # print(url)
        res = eval(res.text).get('data').get('result')

        for e in res:

            clustername = e.get('metric').get('cluster')
            if clustername == cluster:
                # print(e)
                # addr = e.get('metric').get('addr')
                value = e.get('value')[1]

                return value


def topicgather(cluster):
    topic = 0
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('kafka_topic_partitions', checktime,)
    res = requests.get(url)
    if res.status_code == 200:
        # print(url)
        res = eval(res.text).get('data').get('result')

        for e in res:

            clustername = e.get('metric').get('cluster')
            if clustername == cluster:
                # print(e)
                # addr = e.get('metric').get('addr')
                value = e.get('value')[1]
                topic += int(value)
    return value


def consumer_lag(cluster):
    consumer_lst = []
    count = 0
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('kafka_consumergroup_lag', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')

        for e in res:

            clustername = e.get('metric').get('cluster')
            topic = e.get('metric').get('topic')
            partition = e.get('metric').get('partition')

            if clustername == cluster and topic != '__consumer_offsets':
                value = int(e.get('value')[1])
                count += 1
                # print(e)
                consumer_lst.append(value)
    # print(consumer_lst)
    return max(consumer_lst)


def jifeikfk():
    all = {}
    jifeikfk = requests.get('http://133.0.124.212:5000/kfk/v1/list')
    res = json.loads(jifeikfk.text)
    for x in res:
        if x:
            ip = x.split(' ')[0]
            total_num = x.split(' ')[-1]
            if ip in ['133.0.209.50', '133.0.209.51', '133.0.209.52', '133.0.209.53', '133.0.209.54', '133.0.209.55',
                      '133.0.209.56', '133.0.209.57', '133.0.209.58', ]:
                all.update({'采集计费A' + ip: [total_num, ]})
            else:
                all.update({'5G计费B' + ip: [total_num, ]})
    return all


def kafka_res():
    res_dic = {}
    for cluster in kfk_clsname():
        kfk = kfkgather(cluster)
        topic = topicgather(cluster)
        lag = consumer_lag(cluster)
        res_dic.update({cluster: [kfk, topic, lag]})

    res_dic.update(jifeikfk())
    return res_dic
    # return res_dic.update(jifeikfk())


if __name__ == '__main__':
    print(kafka_res())
# print(jifeikfk())
