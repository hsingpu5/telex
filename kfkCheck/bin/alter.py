#!/bin/bash/env python3

import requests  # pip3 install requests -i https://pypi.douban.com/simple
import json
import sys

url = 'http://133.0.206.49:9093/api/v1/alerts'
headers = {
    'content-type': 'application/json',
}

try:
    ip = sys.argv[1]
    # 脚本执行传入的参数  例如:来自zbx的shell脚本调用  传入第二个参数为报警标题 第三个为报警内容
    summary = sys.argv[2]
    description = sys.argv[3]
    paasServiceName = sys.argv[4]
except IndexError as e:
    ip = 'without_ip'
    description = 'without_description'


def alterinfo(ip, summary, description, paasServiceName="CRM3-AMC"):
    data = [
        {
            "labels": {
                "instance": ip,
                "serverity": "warning",
                "cluster": "amc",
                "alertType": "amc_change",
                "alertname": "amc_alert",
                "paasServiceName": paasServiceName
            },
            "annotations": {
                "description": description,
                "summary": summary
            }
        }
    ]

    response = requests.post(url, headers=headers, json=data)
    print(response.content)
    return response.content


if __name__ == '__main__':
    # if ip:
    #    print(ip, summary, description, paasServiceName)
    alterinfo(ip, summary, description, paasServiceName)
