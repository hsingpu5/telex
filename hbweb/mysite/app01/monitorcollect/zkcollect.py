# zookeeper monitor information

import requests
from app01.views import checktime
import json

zkinfo = {}
zk_lst = set()
zkurl = (
    'http://133.0.206.49:9516',
)


def zkgather(cluster):
    for i in zkurl:
        url_t = 'http://133.0.206.49:9516/api/v1/query?query=zk_up&time=1655129309.095&_=1655129118105'

        url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('zk_up', checktime,)

        res = requests.get(url_t)
        if res.status_code == 200:

            res = eval(res.text).get('data').get('result')

            for e in res:
                print(e)
                clustername = e.get('metric').get('cluster')
                if clustername == cluster:
                    addr = e.get('metric').get('addr')

                    zk_lst.add(str(addr))
            return len(zk_lst)


if __name__ == '__main__':
    print(zkgather('csf'))
