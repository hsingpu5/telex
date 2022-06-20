from django.shortcuts import render, HttpResponse
import requests
import time
from app01.monitorcollect.zkcollect import zookeeper_res
from app01.monitorcollect.ngxcollect import nginx_res
from app01.monitorcollect.rediscollect import redis_res
from app01.monitorcollect.kafkacollect import kafka_res
from app01.monitorcollect.escollect import es_res


# from app01.monitorcollect.ipscollect import ips_res


# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    return render(request, "user_list.html")


def user_add(request):
    return HttpResponse("add")


def tpl(request):
    name = 'hp'
    roles = ["管理员", "ceo", "baoan"]
    user_info = {"name": "xp", "salary": 3000, "role": 'cto'}
    data_list = [
        {"name": "xp", "salary": 3000, "role": 'cto'},
        {"name": "xp", "salary": 3000, "role": 'cto'},
        {"name": "xp", "salary": 3000, "role": 'cto'},
    ]
    return render(request, "tpl.html", {"n1": name, "n2": roles, "n3": user_info,
                                        "n4": data_list})


def news(request):
    res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/06/news")
    data_lst = res.json()
    print(data_lst)
    return render(request, "news.html")


def something(request):
    # request对象,封装了用户发送过来的所有请求相关数据
    return HttpResponse('someth')


data_dic = {'nginx': nginx_res(), 'kafka': kafka_res(), 'zookeeper': zookeeper_res(), 'redis': redis_res(),
            'es': es_res(), 'ips': {'IPS': ['√', '√', '√']}}

# checktime = str(time.time())[0:14]

print(data_dic)


def mr(request):
    print(data_dic)
    return render(request, 'mrs.html', {"data_dic": data_dic})
