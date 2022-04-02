import os, sys
from elasticsearch import Elasticsearch
from datetime import datetime
import json

BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
sys.path.insert(0, BASE_DIR)
from conf import es_auth

write_list = []
# es连接信息

es = Elasticsearch(["133.0.120.198:9200"], http_auth=es_auth)
# es查询语句信息
apiName = "湖北根据产品实例ID判断产品是否为5G"
mtime = "now-60s"
body = {
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "apiName": apiName
                    }
                },
                {
                    "range": {
                        "@timestamp": {
                            "gte": mtime,
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
    return "eopstat-" + now


def logfilename():
    # now = datetime.now().strftime('%Y.%m.%d--%H.%M.%S')
    now = datetime.now().strftime('%Y.%m.%d')
    return r'D:\code\telex\es\logs\\' + now + '.log'


def getinfo(indexname, body):
    '''执行查询'''
    # res = es.get(index=indexname, body=body)
    res = es.search(index=indexname, body=body)

    return json.dumps(res, ensure_ascii=False)
    # return res


def writefile(info):
    if not info: return
    res = logfilename()
    with open(res, mode='a', encoding='utf-8') as f:
        for i in info:
            f.write(str(i) + '\n')


def ana():
    '''
    解析查询到的文本内容
    :return:
    '''
    k1 = 'apiName'
    k2 = 'timestamp'
    indexname = getindexname()  # 获取当前索引名
    res = getinfo(indexname, body)  # 传入索引名 及查询语句
    res = json.loads(res)
    res = res.get("hits").get("hits")

    for i in res:
        # print('hits内容:', i)
        info = i.get('_source').get(k1)
        tm = i.get('_source').get(k2)
        tm = str(tm)[0:10]
        tm = datetime.fromtimestamp(int(tm))
        tm = tm.strftime('%Y-%m-%d %H:%M:%S')
        write_dic = {k2: tm, k1: info}
        # print(write_dic)
        write_list.append(write_dic)
    return write_list


if __name__ == '__main__':
    res = ana()
    print(res)
    writefile(res)  # 写入文件
