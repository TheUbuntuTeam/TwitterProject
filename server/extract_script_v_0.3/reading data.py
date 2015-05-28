import json
import panda
import matplotlib.pyplot as plt

#twitter data path
tweets_data_path = '~/project_work/TwitterProject/server/extract_script_v_0.3/log.json'

#create an array and fill it with data
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

#print the number of tweets stored in
print(len(tweets_data))

#structure the tweets data into a pandas DataFrame
tweets = panda.DataFrame()

tweets['user' = map(lampda tweet: tweet['user'], tweets_data)
tweets['text' = map(lampda tweet: tweet['text'], tweets_data)

