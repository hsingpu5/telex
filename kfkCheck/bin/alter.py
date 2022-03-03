#!/bin/bash/env python3

import requests  # pip3 install requests -i https://pypi.douban.com/simple
import json

headers = {
    'content-type': 'application/json',
}

url = 'http://133.0.206.49:9093/api/v1/alerts'


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
