from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import time
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
 
start_time = time.time() #grabs the system time
keyword_list = ["PYTHON" , "JAVA" , "JAVASCRIPT" , "RUBY" , "COBOL" , "C#" , "OBJECTIVE C" , "C++" , "ASSEMBLY" , "PERL" , "SCALA" , "VISUALBASIC"] #track list

class listener(StreamListener):
 
	def on_data(self, data):
 
		#while True:
		saveFile = open('log.txt', 'a')
		decoded = json.loads(data)
		try:
			msg = ('%s$ %s$ %s' % (decoded['user']['time_zone'],decoded['user']['location'],decoded['text']))
			#msg = ('LOCATION: %s TIME_ZONE: %s TWEET_MESSAGE: %s ' % (decoded['user']['location'].encode('ascii', 'ignore'),decoded['user']['time_zone'], decoded['text'].encode('ascii', 'ignore')))
			#msg_no_encode = ('USER: @%s --> LOCATION: %s TWEET_MESSAGE: %s' % (decoded['user']['screen_name'], decoded['user']['location'], decoded['text']))
			print(msg) 
			#print(msg_no_encode)
			print("\n")
			saveFile.write(msg)
			saveFile.write('\n')
			saveFile.close()

			return True
				
		except UnicodeEncodeError:
			return False


		except BaseException as e:
			print('failed ondata,', str(e))
			time.sleep(5)
			return True
 
		#exit()
 
	def on_error(self, status):
 
		print(status)
		
#OAuth object
auth = OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)


def start_stream(): 
	while True:
		try:
			twitterStream = Stream(auth, listener(start_time)) #initialize Stream object with a time out limit
			twitterStream.filter(track=keyword_list)  #call the filter method to run the Stream Object
		except:
			continue
#~ 
if __name__ == "__main__":

	start_stream()
