from app.kafka.kafka import get_consumer


def topic_subscriber(topic_name:str = 'com.persistance.test'):
    c= get_consumer()
    c.subscribe([topic_name])

    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print('Received message: {}'.format(msg.value().decode('utf-8')))

    c.close()