# nginx monitor information

import requests, time

data = {
    'user': 'admin',
    'password': 'cvUx3#pmq_u',
    'email': '',
}
session = requests.Session()

login = session.post(url='http://133.0.206.49:9511/login', data=data)


rule = 'nginx_vts_upstream_requests_total'
endtime = str(time.time())[0:10]
starttime = str(time.time() - 300)[0:10]

url = 'http://133.0.206.49:9516/api/v1/query?query=nginx_vts_upstream_requests_total&time=1655434705.445&_=1655434277860' % (rule,
                                                                                                     starttime, endtime)
print(url)

def ngxgather(cluster):
    res = requests.get(url)
    print(res.status_code)
    if res.status_code == 200:
      #  print(res.text)
        res = eval(res.text).get('data').get('result')

        for e in res:
            # print(e)
            clustername = e.get('metric').get('cluster')
            if clustername == cluster:
                addr = e.get('metric').get('addr')
                value = e.get('value')[1]

        return


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
        # print(zk_dic)

        live = 0
        for i in zk_dic.values():
            live += int(i)
        return [len(zk_dic), live]


def max_latency(cluster):
    zk_lst = []
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('zk_max_latency', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')

        for e in res:
            # print(e)
            clustername = e.get('metric').get('cluster')
            if clustername == cluster:
                value = e.get('value')[1]

                zk_lst.append(int(value))
    # print(zk_lst)

    return max(zk_lst)


def zk_outstanding_requests(cluster):
    zk_lst = []
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('zk_outstanding_requests', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')

        for e in res:
            #  print(e)
            clustername = e.get('metric').get('cluster')
            if clustername == cluster:
                value = e.get('value')[1]

                zk_lst.append(int(value))

    return sum(zk_lst)


def zk_num_alive_connections(cluster):
    zk_lst = []
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s' % ('zk_num_alive_connections', checktime,)
    res = requests.get(url)
    if res.status_code == 200:

        res = eval(res.text).get('data').get('result')

        for e in res:
            # print(e)
            clustername = e.get('metric').get('cluster')
            if clustername == cluster:
                value = e.get('value')[1]

                zk_lst.append(int(value))

    return max(zk_lst)


clusternames = [
    'csf',
    'databus',
    'ddal',
    'mlcache',
    'hlog',
    '计费ABM集群ZK',
    '计费批价荆州武汉ZK',
    '计费批价采集ZK',
    '计费批价策略ZK',
    '计费账务DUBBO-A',
    '计费账务DUBBO-B',
    '计费账务DUBBO-C',
    '计费支付DUBBO-A',
    '计费支付DUBBO-B',

]


def zookeeper_res():
    res = {}
    for cluster in clusternames:
        live = zkgather(cluster)
        max_ = max_latency(cluster)
        req = zk_outstanding_requests(cluster)
        conn = zk_num_alive_connections(cluster)
        res.update({cluster: [live, max_, req, conn, ]})
    return res


if __name__ == '__main__':
    ngxgather('a')
    # print(zookeeper_res())
