import os, sys
from elasticsearch import Elasticsearch
from datetime import datetime
import json

BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
sys.path.insert(0, BASE_DIR)
from conf import es_auth

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
    return "eopstat-" + now


def logfilename():
    # now = datetime.now().strftime('%Y.%m.%d--%H.%M.%S')
    now = datetime.now().strftime('%Y.%m.%d')
    return r'D:\code\telex\es\logs\\' + now + '.log'


def getinfo(index_name, body_name):
    '''执行查询'''
    # res = es.get(index=indexname, body=b)
   # print('-------------------')
   # print(index_name, body_name)
    #print('------------------')
    res = es.search(index=index_name, body= body_name)

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
    #print(res)

    res = res.get("hits").get("hits")
    #
    for i in res:

          info = i.get('_source').get('rawRequest')
          print(info)
          #index=info.index('验')
          #print(info[index:10])
    #     tm = i.get('_source').get(k2)
    #     tm = str(tm)[0:10]
    #     tm = datetime.fromtimestamp(int(tm))
    #     tm = tm.strftime('%Y-%m-%d %H:%M:%S')
    #     write_dic = {k2: tm, k1: info}
    #     # print(write_dic)
    #     write_list.append(write_dic)
    #return write_list


if __name__ == '__main__':
    print(ana())
