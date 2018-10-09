
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient


from tweepy.streaming import StreamListener
import tweepy

#Variables that contains the user credentials to access Twitter API 
access_token = "access_token"
access_token_secret = "access_token_secret"
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"


class TweeterStreamListener(StreamListener):
    """ A class to read the twitter stream and push it to Kafka"""

    def on_data(self, data):
        """ This method is called whenever new data arrives from live stream.
        We asynchronously push this data to kafka queue"""
        #msg =  status.text.encode('utf-8')
        try:
            #self.producer.send_messages('test', msg)
            producer.send_messages("topicname", data.encode('utf-8'))# publish messages to this topicname from the twitter
            print(data)
        except Exception as e:
            print(e)
            return False
        return True

    def on_error(self, status_code):
        print("Error received in kafka producer")
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream

if __name__ == '__main__':

    kafka = KafkaClient("localhost:9092")
    producer = SimpleProducer(kafka)
    l = TweeterStreamListener() #instance of class

    # Create Auth object
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create stream and bind the listener to it
    stream = Stream(auth, l)

    #Custom Filter rules pull all traffic for those filters in real time.
    #stream.filter(track = ['love', 'hate'], languages = ['en'])
    stream.filter(track='searchkey')# fileter the tweets with the searchkey that you want 