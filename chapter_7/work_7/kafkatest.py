from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers = 'localhost:9092',
    value_serializer= lambda v : json.dumps(v).encode('utf-8'),
    

)
data = {
    "name": "test_user",
    "age":25,
    "city":"Iasi"
}

while True:
    producer.send("driven_data_stream",value=data)
    print("Trimis:", data)
    time.sleep(2)