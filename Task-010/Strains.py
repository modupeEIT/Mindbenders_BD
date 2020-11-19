from kafka import KafkaProducer
import requests
import json

TOPIC = "weeds"

def ShowStrains():
	datta = requests.get("http://strainapi.evanbusse.com/KPriyQg/strains/search/all")
	data = datta.json()
	producer = KafkaProducer(bootstrap_servers = ['localhost:9092'],value_serializer=lambda m: json.dumps(m).encode('ascii'))
	producer.send(TOPIC, data)
	producer.flush()

ShowStrains()

kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic weeds







