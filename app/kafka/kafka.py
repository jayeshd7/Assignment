

from confluent_kafka import Producer
from confluent_kafka import Consumer
import os

def get_producer():
    p = Producer({'bootstrap.servers': os.getenv("KAFKA_BOOTSTRAP_SERVER",'localhost:9092')})
    return p


def get_consumer():
    c = Consumer({
        'bootstrap.servers': os.getenv("KAFKA_BOOTSTRAP_SERVER",'localhost:9092'),
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    })
    return c
def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def produce_message(message:str, topic:str):
    p = get_producer()
    p.poll(0)
    p.produce(topic, message.encode('utf-8'), callback=delivery_report)
    p.flush()



