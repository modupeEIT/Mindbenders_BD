from kafka import KafkaProducer
import requests
import json

TOPIC = "stocks"

def GetStockval():
	datta = requests.get("https://api.twelvedata.com/time_series?symbol=AAPL&interval=1min&apikey=bde4d36c4bfd414ea21932ba14a2f0ea")
	producer = KafkaProducer(bootstrap_servers = ['localhost:9092'])
	
	data = json.loads(datta.text)

	for row in data["values"]:
		producer.send(TOPIC, json.dumps(row).encode('utf-8'))
		producer.flush()
		print("Data sent to topic!")
GetStockval()
