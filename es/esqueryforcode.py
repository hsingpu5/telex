import os, sys
import time

from elasticsearch import Elasticsearch
from datetime import datetime
import json

BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
sys.path.insert(0, BASE_DIR)
from conf import es_auth

if datetime.now().strftime("%Y") != '2022':
    raise TimeoutError

write_list = []
# es连接信息

es = Elasticsearch(["http://133.0.120.198:9200"], http_auth=es_auth)
phoneid = "18972658999"
mtime = "now-60s"
body = {
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "rawRequest": "18972658999"
                    }
                },
                {
                    "range": {
                        "@timestamp": {
                            "gte": "now-60m",
                            "lte": "now"
                        }
                    }
                }
            ]
        }
    }
}


# print(es.get(index="eopstat-2022.04.02", id='iHFX6H8BWdwWJmouAPZh'))
def getindexname():
    # 获取index名字
    now = datetime.now().strftime('%Y.%m.%d')
    # return "eopstat-" + now
    return 'eopstat*'


def logfilename():
    # now = datetime.now().strftime('%Y.%m.%d--%H.%M.%S')
    now = datetime.now().strftime('%Y.%m.%d')
    return r'D:\code\telex\es\logs\\' + now + '.log'


def getinfo(index_name, body_name):
    '''执行查询'''
    # res = es.get(index=indexname, body=b)
    # print('-------------------')
    # print(index_name, body_name)
    # print('------------------')
    res = es.search(index=index_name, body=body_name)

    return json.dumps(res, ensure_ascii=False)
    # return res


def ana():
    query_res = {}
    '''
    解析查询到的文本内容
    :return:
    '''
    k1 = 'apiName'
    k2 = 'timestamp'
    indexname = getindexname()  # 获取当前索引名
    res = getinfo(indexname, body)  # 传入索引名 及查询语句
    res = json.loads(res)
    # print(res)

    res = res.get("hits").get("hits")
    #
    for i in res:

        info = i.get('_source').get('rawRequest')
        send_time = i.get('_source').get('timestamp')
        findres = info.find('验')
        if findres != -1:
            # print(findres)
            # print(info)
            tm = str(send_time)[0:10]
            tm = datetime.fromtimestamp(int(tm))
            tm = tm.strftime('%Y-%m-%d %H:%M:%S')

            info = info[findres - 17:findres + 20]
            query_res.update({info: tm})
    return query_res


def queryres():
    while True:
        print('链接eop,查询中...')
        res = ana()
        # print(res)
        for k, v in res.items():
            print('#=================================================#')
            print(v)
            print(k)
            # print('\033[1;31;40m%s\033[0m' % v)
            # print('\033[1;32;40m%s\033[0m' %  k)
        time.sleep(60)


queryres()
if __name__ == '__main__':
    pass
