#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, re

original_dir_name = r'C:\Users\hp\Desktop\o2pg\BSSTICKET\导出原始合并all'
res_dir_name = r'C:\Users\hp\Desktop\o2pg\BSSTICKET\res'
lst = os.listdir(original_dir_name)


def o2pg(ora_file, pg_file):
    with open(ora_file, mode='r', encoding='ANSI') as of:
        with open(pg_file, mode='w', encoding='utf-8') as pgf:
            res = of.readlines()
            for line in res:
                # 数据类型替换
                # print(type(line))

                line = re.sub(r"NUMBER\([1-9]\)", 'int4', line)
                line = line.replace('NUMBER', 'numeric')
                #line = line.replace('BINARY_FLOAT', 'float4')
                line = line.replace('TIMESTAMP', 'timestamp')
                line = line.replace('VARCHAR2', 'varchar')
                line = line.replace('CHAR', 'char')
                # 索引替换
                # 分区替换
                # print(line)

                pgf.write(line)


def run():
    for i in lst:
        if i.endswith('tab'):
            oracle_file = os.path.join(original_dir_name, i)
            pgsql_file = os.path.join(res_dir_name, i)
            o2pg(oracle_file, pgsql_file)


if __name__ == '__main__':
    run()

# https://www.postgresql.org/docs/9.1/sql-createindex.html
# http://t.zoukankan.com/star521-p-13489365.html
