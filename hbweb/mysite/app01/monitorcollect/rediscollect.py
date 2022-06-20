# zookeeper monitor information

import requests, time

# from app01.views import checktime
checktime = str(time.time())[0:14]
import json


def redisstatus(cluster):
    zk_dic = {}
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('redis_cluster_state', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')
        print(res)
        for e in res:
            # print(e)
            clustername = e.get('metric').get('cluster')
            if clustername == cluster:

                value = e.get('value')[1]

                if value: return '正常'


def memuser(cluster):
    value = 0
    total = 0
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('redis_memory_used_bytes', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')
        # print(res)
        for e in res:
            # print(e)
            clustername = e.get('metric').get('cluster')

            if clustername == cluster:
                value += int(e.get('value')[1])
    # print(value/1000/1000/1000)
    return str(value / 1000 / 1000 / 1000)[:3] + 'G'


def slots_fail(cluster):
    value = 0

    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('redis_cluster_slots_fail', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')
        # print(res)
        for e in res:
            # print(e)
            clustername = e.get('metric').get('cluster')

            if clustername == cluster:
                value += int(e.get('value')[1])
    # print(value/1000/1000/1000)
    return value


def redis_up(cluster):
    '''主从同步 判定是否up'''
    value = 0

    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('redis_up', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')
        # print(res)
        for e in res:
            # print(e)
            clustername = e.get('metric').get('cluster')

            if clustername == cluster:
                value += int(e.get('value')[1])
                if not value:
                    return 'down'

    # print(value/1000/1000/1000)
    return 'up'


def clusters():
    clusters_set = set()
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('redis_cluster_known_nodes', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')
        # print(res)
        for e in res:
            # print(e)
            clustername = e.get('metric').get('cluster')

            clusters_set.add(clustername)

    # print(value/1000/1000/1000)
    return clusters_set


def redis_res():
    res = {}
    for cluster in clusters():
        mem = memuser(cluster)
        stat = redis_up(cluster)
        sltfail = slots_fail(cluster)
        res.update({cluster: [mem, sltfail, stat]})
    return res


if __name__ == '__main__':
    # print(redisstatus('CRM测试集群缓存246247'))
    # print(memuser('CRM测试集群缓存246247'))
    print(redis_res())
