from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer
from kafka import KafkaClient

ACCESS_TOKEN= ""
CONSUMER_KEY= ""
CONSUMER_SECRET= ""
TOPIC = "tweets"

class ListenerStream(StreamListener):
	def on_data(self,data):
		producer.send_messages(TOPIC, data.encode('utf-8'))
		print(data)

	def on_error(self, status):
		print(status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
listen = ListenerStream()
autho = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
autho.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)
stream = Stream(autho, listen)
stream.filter(track="africa", is_async=True)



