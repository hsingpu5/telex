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


def kafka_res():
    res_dic = {}
    for cluster in kfk_clsname():
        kfk = kfkgather(cluster)
        topic = topicgather(cluster)
        lag = consumer_lag(cluster)
        res_dic.update({cluster: [kfk, topic, lag]})
    return res_dic


if __name__ == '__main__':
    print(kafka_res())
