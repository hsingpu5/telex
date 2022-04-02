from elasticsearch import Elasticsearch
from elasticsearch import helpers
from requests.auth import HTTPBasicAuth
from sqlalchemy import create_engine
import datetime
import time

t = datetime.datetime.today().date()
y = t - datetime.timedelta(days=1)
t = str(t)
y = str(y)
ytimearray = time.strptime(y, "%Y-%m-%d")
ytime = int(time.mktime(ytimearray))
ttimearray = time.strptime(t, "%Y-%m-%d")
ttime = int(time.mktime(ttimearray))

SEARCHCONFIG = {
                   'es': {
                             'address': ** *,
                   'username': ** *,
               'password': '***',
                           'indexlesson': '***',
'indexlessontype': '***',
}
}

class SearchConfig():

    def __init__(self, c):
        self.address = c['es']['address']
        self.auth = [c['es']['username'], c['es']['password']]
        self.indexlesson = c['es']['indexlesson']
        self.indexlessontype = c['es']['indexlessontype']


class Search:
    """
    搜索核心类
    """
    config = None
    es = None

    def __init__(self, config=None):
        if config is not None:
            self.config = config
            self.es = Elasticsearch(self.config.address, http_auth=config.auth)

    def get_all_lesson(self, is_live=1):

        try:
            indexType = self.config.indexlessontype
            res = self.es.get(index=self.config.indexlesson, doc_type=indexType, is_live=is_live)
            # print(res)
        except Exception as e:
            print(e)
            print('false')
            return None

    def get_yeasterday_all(self):

        body = {
            "query": {
                "bool": {
                    "must": {
                        "range": {
                            "learning_time": {
                                "gte": ytime,
                                "lte": ttime

                            }
                        }
                    }
                }
            }
        }

        res = self.es.search(index=self.config.indexlesson, doc_type=self.config.indexlessontype, body=body)
        print(res['hits']['total'])

    def get_yestarday_live(self):
        '''
        得到昨天的直播数
        :return:
        '''

        body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "term": {
                                "is_live": 1
                            }
                        },
                        {
                            "term": {
                                "is_online": 1
                            }
                        },
                        {
                            "range": {
                                "learning_time": {
                                    "gte": ytime,
                                    "lte": ttime

                                }
                            }
                        }

                    ]

                },

            }
        }

        res = self.es.search(index=self.config.indexlesson, doc_type=self.config.indexlessontype, body=body)
        print(res['hits']['total'])

    def get_yesterday_no_live(self):

        body = {
            "query": {
                "bool": {
                    "must": [{
                        "range": {
                            "learning_time": {
                                "gte": ytime,
                                "lte": ttime

                            }
                        }
                    },
                        {
                            "bool": {
                                "should": [{
                                    "term": {
                                        "is_live": 0
                                    }

                                },
                                    {
                                        "term": {
                                            "is_live": 0
                                        }
                                    }

                                ],

                            }
                        }

                    ]
                }
            }
        }

        res = self.es.search(index=self.config.indexlesson, doc_type=self.config.indexlessontype, body=body)
        print(res['hits']['total'])


#
config = SearchConfig(SEARCHCONFIG)
search = Search(config)
search.get_yeasterday_all()
search.get_yestarday_live()
search.get_yesterday_no_live()
# ————————————————
# 版权声明：本文为CSDN博主「NoOne-csdn」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_40161254/article/details/85126682
