from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer
from kafka import KafkaClient

ACCESS_TOKEN= "53391472-UZwR7vCTEhsWuqrMGhimEnJ1xW2rRmxYIDPIMCuIu"
TOKEN_SECRET= "zi9ml88hYzsuKDqzlYgjApk2TPFWcCFgml5Qn7ws9N1rn"
CONSUMER_KEY= "knb14poGcKpoNdbq6QzNebfzs"
CONSUMER_SECRET= "aoKZMRHrchhwEI5WUm18MHnCDeX0X2dBgrwj1Mq7Fhw7x37bfM"
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



