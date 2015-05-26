import tweepy
from tweepy import auth
#from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
#from tweepy import Stream
from tweepy import API




#get credentials' file (change it with your path)
credentials = open('/users/MICHELE/project_work/TwitterProject/.credentials', 'r')

#get and split the credentials
def readerCredentials():
	for line in credentials.read().splitlines():
		yield line 

#the credentials file must be in order: consumer_key, consumer_secret, access_token, access_token_secret
key = readerCredentials()
consumer_key = key.__next__()
consumer_secret = key.__next__()
access_token = key.__next__();
access_token_secret = key.__next__()
credentials.close()

#authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#here search for the specified query
query = 'python -animal'
#searched_tweets = [status for status in tweepy.Cursor(api.search, q=query)]

for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
	print(tweet.text)



#~ for line in searched_tweets
	#~ new_file = "searched_tweets.txt"
	#~ with open(new_file, 'w') as out:
		#~ out.write(search_result.split())
		#~ out.close()
