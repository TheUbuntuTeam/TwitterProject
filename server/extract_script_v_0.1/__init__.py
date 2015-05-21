import tweepy
from tweepy import auth
from tweepy import OAuthHandler
from tweepy import API
import sys

#get credentials' file (change it with your path)
credentials = open('/home/marco/project_work/TwitterProject/.credentials', 'r')

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

def get_tweets(query):
	#here search for the specified query in input
	query = "PYTHON -animal" or "JAVA" or "PHP" or "JAVASCRIPT" or "RUBY" or "SHELL" or "BASH" or "COBOL" or "CLOJURE" or "C" or "C#" or "OBJECTIVE C" or "C++" or "ASSEMBLY" or "PERL" or "LUA" or "SCALA" or "GO" or "VISUALBASIC" or "SWIFT"

	for tweet in tweepy.Cursor(api.search, q=query).items():
		print(tweet.text)

#~ searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items()]
#~ 
#~ for line in searched_tweets:
	#~ new_file = "searched_tweets.txt"
	#~ with open(new_file, 'w') as out:
		#~ out.write(search_result.split())
		#~ out.close()


if __name__ == '__main__':
	results = get_tweets('')
	#save_tweets(results, 'tweets.txt')
