import os, sys
from elasticsearch import Elasticsearch
from datetime import datetime
import json

BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
sys.path.insert(0, BASE_DIR)
from conf import es_auth

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
    now = datetime.now().strftime('%Y.%m.%d--%H.%M.%S')
    return r'D:\code\telex\es\logs\\' + now + '.log'


def getinfo(indexname, body):
    '''执行查询'''
    # res = es.get(index=indexname, body=body)
    res = es.search(index=indexname, body=body)
    return json.dumps(res, ensure_ascii=False)
    # return res


def writefile(info):
    res = logfilename()
    with open(res, mode='w+', encoding='utf-8') as f:
        f.write(info)


indexname = getindexname()  # 获取当前索引名
res = getinfo(indexname, body)  # 传入索引名 及查询语句
print(res)
writefile(res)  # 写入文件
if __name__ == '__main__':
    pass
