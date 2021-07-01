
from kafka import KafkaProducer
import json
from ServerLog import get_server_log
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_server_log()
        print(registered_user)
        producer.send("registered_user", registered_user)
        time.sleep(3)
