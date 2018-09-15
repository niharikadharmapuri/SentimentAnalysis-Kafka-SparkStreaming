#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

#Variables that contains the user credentials to access Twitter API 
access_token = "1039969684383309824-DjhWTyti7KeukoLKzJbLq2Ix0pyNZt"
access_token_secret = "TehO70B3FQQj0C9R0442Uh6FoXV8mhRp137er7eEMr2SK"
consumer_key = "Vv5dEOfjSUdpl4mdeirxkyTiQ"
consumer_secret = "1wVqK9uoBoSP4d5NFKSRDjShQqjAt0LvRPmuNiSkj2tmhGiroj"


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