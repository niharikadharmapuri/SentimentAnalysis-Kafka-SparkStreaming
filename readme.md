# Twitter Sentiment Analysis using Kafka:
This project uses Twitter API to get the tweets and store them in Kafka server. Then perform sentiment analysis of real-time tweets.

## The project has following files:


## Prerequisites:
1. Twitter API credentials
2. Kafka


## Installation:
You need to install Kafka using<br/>
		`pip install `

You need to install dependent packages from requirements.txt using<br/>
	`pip install -r requirements.txt`

## Running the Project:

1. start zookeeper:
		$ bin/zookeeper-server-start.sh config/zookeeper.properties
		
2. Start Kafka:
   You need to edit the config files to specify the sink, the source
		 $ bin/kafka-server-start.sh config/server.properties
3. create a topic called tweets
		$ bin/kafka-topics.sh --create --zookeeper --partitions 1 --topic tweets localhost:2181 --replication-factor 1
