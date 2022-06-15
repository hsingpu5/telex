# zookeeper monitor information

import requests
from app01.views import checktime
import json


def zkgather(cluster):
    zk_dic = {}
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('zk_up', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')

        for e in res:
            # print(e)
            clustername = e.get('metric').get('cluster')
            if clustername == cluster:
                addr = e.get('metric').get('addr')
                value = e.get('value')[1]

                zk_dic.update({addr: value})
        print(zk_dic)

        live = 0
        for i in zk_dic.values():
            live += int(i)
        return len(zk_dic), live


if __name__ == '__main__':
    print(zkgather('csf'))
