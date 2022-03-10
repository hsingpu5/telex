from kafka import KafkaConsumer

from kafka.errors import kafka_errors
import traceback
import json


def consummer_demo():
    consumer = KafkaConsumer(
        'MNT_EVENT_CLOUD_DEFAULT',
        bootstrap_servers='133.0.177.112:9092',
        group_id='test'
    )

    for message in consumer:
        print("recevive, {}".format(
            message
            # json.load(message)
        ))


if __name__ == '__main__':
    consummer_demo()