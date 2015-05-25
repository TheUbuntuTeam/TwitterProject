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
'''The streaming api is quite different from the REST api because the REST api is used to pull data from twitter but the streaming api pushes messages to a persistent session. This allows the streaming api to download more data in real time than could be done using the REST API.'''

class TweepyFileListener(tweepy.StreamListener):
	
	def on_status(self, status):
		print(status.text)
		
	def on_data(self, data):
		# Twitter returns data in JSON format - we need to decode it first
		decoded = json.loads(data)
		#convert UTF-8 to ASCII ignoring all bad characters sent by users
		msg = ('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
		print(msg)
		saveFile = open("log.txt", 'a')
		saveFile.write(data)
		saveFile.write('\n')
		saveFile.close()
		return True
		    
	def on_error(self, status_code):
		if status_code == 420:
			#returning False in on_data disconnects the stream
			return False

if __name__ == "__main__":
	TweepyFileListener()
