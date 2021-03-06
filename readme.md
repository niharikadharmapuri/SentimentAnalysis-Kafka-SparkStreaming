# Twitter Sentiment Analysis using Kafka:
This project uses Twitter API to get the tweets and store them in Kafka server. Then perform sentiment analysis of real-time tweets.

## The project has following files:


## Prerequisites:
1. Twitter API credentials- Get a developers account and create an App and get the credentials.
2. Kafka
3. You need to have Java installed.


## Installation:
You need to install Kafka using<br/>
	https://kafka.apache.org/quickstart

You need to install dependent packages from requirements.txt using<br/>
	`sudo pip install -r requirements.txt`

## Running the Project:
Go to the kafka home and do the following

1. start zookeeper in one terminal tab:
		$ cd kafka_2.11-2.0.0
		$ bin/zookeeper-server-start.sh config/zookeeper.properties
		
2. Start Kafka in another terminal tab:
		 $ bin/kafka-server-start.sh config/server.properties

3. create a topic called tweets
		$ bin/kafka-topics.sh --create --zookeeper --partitions 1 --topic topicname localhost:2181 --replication-factor 1

4. Run the filename.py to store the tweets into Kafka cluster
		python filename.py

5. To check if the topics are getting published in Kafka,
		bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topicname --from-beginning