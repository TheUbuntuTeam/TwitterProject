import tweepy
from tweepy import auth
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json

#get credentials' file (change it with your path)
# !!! DO NOT PUBLISH YOUR PRIVATE KEYS ONLINE !!!
credentials = open('/home/marco/Documenti/.credentials', 'r')

#get and split the credentials
def getCredentials():
	for line in credentials.read().splitlines():
		yield line 

#the credentials file must be in order: consumer_key, consumer_secret, access_token, access_token_secret
key = getCredentials()
consumer_key = key.__next__()
consumer_secret = key.__next__()
access_token = key.__next__();
access_token_secret = key.__next__()
credentials.close()

#authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#define the api
api = tweepy.API(auth)

#call the class listener
class MyStreamListener(tweepy.StreamListener):
	
	def on_status(self, status):
		print(status.text)
		
	def on_data(self, data):
		# Twitter returns data in JSON format - we need to decode it first
		decoded = json.loads(data)
		#convert UTF-8 to ASCII ignoring all bad characters sent by users
		print ('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
		print ('')
		return True

	def on_error(self, status_code):
		if status_code == 420:
			#returning False in on_data disconnects the stream
			return False
        

def get_tweets():
	stream = Stream(auth, MyStreamListener())
	result = stream.filter(track=["PYTHON -animal" or "JAVA" or "PHP" or "JAVASCRIPT" or "RUBY" or "COBOL" or "C" or "C#" or "OBJECTIVE C" or "C++" or "ASSEMBLY" or "PERL" or "SCALA" or "GO" or "VISUALBASIC"])

def save_tweets():
	d_file = "tweets.txt"
	for line in result:
		with open(d_file, 'a+') as out:
			out.write(result)
			out.close
		
#main
if __name__ == '__main__':
	result = get_tweets()
	save_tweets()
