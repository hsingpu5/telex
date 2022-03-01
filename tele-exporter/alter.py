#!/bin/bash/env python3

import requests  # pip3 install requests -i https://pypi.douban.com/simple
import json

headers = {
    'content-type': 'application/json',
}

url = 'http://133.0.206.49:9093/api/v1/alerts'

summary = 'kfk报警测试(请忽略)'
description = '133.0.124.212 测试信息123'
severity = "warning"
cluster = "amc"
alertType = "amc_change"
alertname = "amc_alert"
paasServiceName = "CRM3-AMC"
data = [
    {
        "labels": {
            "instance": "133.x.x.212",
            "serverity": "warning",
            "cluster": "amc",
            "alertType": "amc_change",
            "alertname": "amc_alert",
            "paasServiceName": "kfk-test"
        },
        "annotations": {
            "description": "kfk报警测试请忽略  ",
            "summary": "kfk报警测试"
        }
    }
]

response = requests.post(url, headers=headers, json=data)
print(response.content)
