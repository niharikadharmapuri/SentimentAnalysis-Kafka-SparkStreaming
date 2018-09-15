#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient
import os


#Variables that contains the user credentials to access Twitter API 
access_token = "access_token"
access_token_secret = "access_token_secret"
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        producer.send_messages("trump", data.encode('utf-8'))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    kafka = KafkaClient("localhost:9092")
    producer = SimpleProducer(kafka)
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #This line filter Twitter Streams to capture data by the keywords: 'trump'
    stream.filter(track='trump')