from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import kafka_errors
import traceback
import json

prokfkserver = '133.0.177.112:9092'
testkfkserver = '133.0.124.212:19092'


# def producer_demo():
#     # 假设生产的消息为键值对（不是一定要键值对），且序列化方式为json
#     producer = KafkaProducer(
#         bootstrap_servers=['localhost:9092'],
#         key_serializer=lambda k: json.dumps(k).encode(),
#         value_serializer=lambda v: json.dumps(v).encode())
#     # 发送三条消息
#     for i in range(0, 3):
#         future = producer.send(
#             'kafka_demo',
#             key='count_num',  # 同一个key值，会被送至同一个分区
#             value=str(i),
#             partition=1)  # 向分区1发送消息
#         print("send {}".format(str(i)))
#         try:
#             future.get(timeout=10) # 监控是否发送成功
#         except kafka_errors:  # 发送失败抛出kafka_errors
#             traceback.format_exc()
def consumer_demo():
    consumer = KafkaConsumer(
        'MNT_EVENT_CLOUD_DEFAULT',
        bootstrap_servers=prokfkserver,
        group_id='test'
    )
    # for message in consumer:
    #     print("receive, key: {}, value: {}".format(
    #         json.loads(message.key.decode()),
    #         json.loads(message.value.decode())
    #         )
    #     )
    for message in consumer:
        # print(message)
        # print(json.loads(message.value.decode()))
        print(message.value.decode())
        break


if __name__ == '__main__':
    consumer_demo()
