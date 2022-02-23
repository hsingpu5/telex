#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import redis  # 安装python的redis模块  pip install redis 或离线安装
import time
import datetime

abspath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, abspath)
logfile = os.path.join(abspath, 'logs/redis_check.log')
host = '133.0.124.212'
port = 6379
db = 0
pwd = 'foobared'
rds = redis.StrictRedis(host, port, db, password=pwd)

# rds = redis.Redis(connection_pool=pool)
rds.set('foo', 'bar33', ex=3)


def redis_check(k, interval=60):
    # rsl = rds.get(k)
    while True:
        rsl = rds.exists(k)
        # print(rsl)

        if rsl:
            print(datetime.datetime.now(), 'key is exists')
            with open(file=logfile, mode='a', encoding='utf-8') as f:
                f.write(str(datetime.datetime.now()) + 'key is exists\r\n')
        else:
            print(datetime.datetime.now(), 'key is missing')
            with open(file=logfile, mode='a', encoding='utf-8') as f:
                f.write(str(datetime.datetime.now()) + 'key is missing\r\n')
            # break
        time.sleep(interval)


if __name__ == '__main__':
    key = 'foo'
    interval = 1
    redis_check(key, interval)
