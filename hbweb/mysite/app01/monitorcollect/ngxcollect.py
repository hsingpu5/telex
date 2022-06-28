# nginx monitor information

import requests, time

rule = 'nginx_vts_upstream_requests_total'
endtime = str(time.time())[0:10]
starttime = str(time.time() - 300)[0:10]

clusters = {
    'CRM顶层': ['133.0.208.45', '133.0.208.46'],
    'EOP顶层': ['133.0.207.187', '133.0.207.186'],
    '计费账务支付顶层': ['133.0.209.139', '133.0.209.140'],
    '计费查询中心顶层': ['133.0.207.157', '133.0.207.158'],
    'CRM辅助服务顶层': ['133.0.207.145', '133.0.207.146'],

}


def total(cluster):
    total = 0
    count = 0
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s&_=%s' % ('nginx_vts_upstream_requests_total',
                                                                           starttime, endtime)

    res = requests.get(url)
    # print(res.status_code)
    if res.status_code == 200:
        # print(res.text)
        print(url)
        res = eval(res.text).get('data').get('result')
        # print(res)
        for e in res:
            # print(e)
            # print( e.get('metric').get('instance') )
            ip = e.get('metric').get('instance').split(':')[0]
            # print(ip)
            if ip in cluster:
                # print(e)
                code = e.get('metric').get('code')
                value = int(e.get('value')[1])
                if code == 'total':
                    total += value
                    count += 1
    return total / count


def ngxgather(cluster):
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    count = 0
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s&_=%s' % ('nginx_vts_upstream_requests_total',
                                                                           starttime, endtime)
    print('url排查', url)
    res = requests.get(url)
    # print(res.status_code)
    if res.status_code == 200:
        # print(res.text)
        print(url)
        res = eval(res.text).get('data').get('result')
        # print(res)
        for e in res:
            # print(e)
            # print( e.get('metric').get('instance') )
            ip = e.get('metric').get('instance').split(':')[0]
            # print(ip)
            if ip in cluster:
                # print(e)
                code = e.get('metric').get('code')
                value = int(e.get('value')[1])
                if code.startswith('2'):
                    sum2 += value
                elif code.startswith('3'):
                    sum3 += value
                elif code.startswith('4'):
                    sum4 += value
                elif code.startswith('5'):
                    sum4 += value
                count += 1
    # print(cluster,sum2, sum4, sum5)
    # res = {cluster: [sum2, sum4, sum5]}
    # return str(int(sum2 / count / 20 / 1000)), int(sum3 / count / 20 / 1000), int(sum4 / count / 20 / 1000), int(
    # sum5 / count / 20 / 1000)
    if sum2: return 'OK'


def request_seconds_total(cluster):
    all = 0
    count = 0
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s&_=%s' % ('nginx_vts_upstream_request_seconds_total',
                                                                           starttime, endtime)
    res = requests.get(url)
    # print(res.status_code)
    if res.status_code == 200:
        # print(res.text)
        print(url)
        res = eval(res.text).get('data').get('result')
        # print(res)
        for e in res:

            # print(e)
            # print( e.get('metric').get('instance') )
            ip = e.get('metric').get('instance').split(':')[0]
            # print(ip)
            if ip in cluster:
                # print(e)
                # code = e.get('metric').get('code')
                value = e.get('value')[1].split('.')[0]
                # print(type(value), value)
                # print(code, value)
                # if code == '2xx':
                all += int(value)
                count += 1
    c = total(cluster)
    print(all, count, c)
    # print(cluster,sum2, sum4, sum5)
    # res = {cluster: [sum2, sum4, sum5]}
    return (str(all / c / count))[:5] + 's'


def main_connections(cluster):
    total = 0
    count = 0
    url = 'http://133.0.206.49:9516/api/v1/query?query=%s&time=%s&_=%s' % ('nginx_vts_upstream_requests_total',
                                                                           starttime, endtime)

    res = requests.get(url)
    # print(res.status_code)
    if res.status_code == 200:
        # print(res.text)
        print(url)
        res = eval(res.text).get('data').get('result')
        # print(res)
        for e in res:
            # print(e)
            # print( e.get('metric').get('instance') )
            ip = e.get('metric').get('instance').split(':')[0]
            # print(ip)
            if ip in cluster:
                # print(e)
                code = e.get('metric').get('code')
                value = int(e.get('value')[1])
                if code == 'total':
                    total += value
                count += 1
    # print(cluster,sum2, sum4, sum5)
    # res = {cluster: [sum2, sum4, sum5]}
    return str(int(total / 1000 / 1000)) + 'Bil'


def nginx_res():
    all = {}
    for k, v in clusters.items():
        print('kv值排查', k, v)
        try:
            all.update({k: [ngxgather(v), request_seconds_total(v), main_connections(v)]})
        except Exception:
            pass
    return all


if __name__ == '__main__':
    # cluster = ['133.0.208.45']
    # print(request_seconds_total(cluster))
    # print(zookeeper_res())
    print(nginx_res())
