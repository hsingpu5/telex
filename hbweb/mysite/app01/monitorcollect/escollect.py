# zookeeper monitor information

import requests, time

# from app01.views import checktime
checktime = str(time.time())[0:14]
import json


def esnode():
    zk_dic = {}
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % (
        'elasticsearch_cluster_health_number_of_nodes', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')

        for e in res:
            print(e)
            clustername = e.get('metric').get('cluster')

            value = e.get('value')[1]

            return value


def esdatanode():
    zk_dic = {}
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % (
        'elasticsearch_cluster_health_number_of_data_nodes', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')

        for e in res:
            print(e)
            clustername = e.get('metric').get('cluster')

            value = e.get('value')[1]

            return value


def es_status():
    zk_dic = {}
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % (
        'elasticsearch_cluster_health_status', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')

        for e in res:
            print(e)
            clustername = e.get('metric').get('cluster')

            value = e.get('value')[1]
            color = e.get('metric').get('color')
            if color == 'red' and value=='1':
                return 'unknown'
    return 'Green'


#
def es_res():
    res = {'es': [es_status(), esnode(), esdatanode(), ]}
    return res


if __name__ == '__main__':
    print(es_res())
