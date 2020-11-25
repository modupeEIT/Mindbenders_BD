from kafka import KafkaProducer
from kafka import KafkaConsumer
import requests
import json

TOPIC = "weeds1"

def GetStrains():
	for i in range(1,2163):
		datta = requests.get("http://strainapi.evanbusse.com/******/strains/data/desc/" + str(i))
		producer = KafkaProducer(bootstrap_servers = ['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
		producer.send(TOPIC, datta.json())
		producer.flush()
GetStrains()









