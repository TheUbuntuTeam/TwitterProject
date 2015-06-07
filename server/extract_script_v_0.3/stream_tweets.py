from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import time
import json

import logging

import logentries
logger = logging.getLogger('logentries')
logger.addHandler(
    logentries.LogentriesHandler('6e11796c-26cd-40c6-8957-30bebf0a5ef0')
)
logger.setLevel(logging.INFO)

#get credentials' file (change it with your path)
# !!! DO NOT PUBLISH YOUR PRIVATE KEYS ONLINE !!!
credentials = open('C:/Users/Emi/Documents/credentials.txt', 'r')

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
<<<<<<< HEAD
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
=======
keyword_list = [" PYTHON " , " JAVA " , " JAVASCRIPT " , " RUBY " , " C# ", " C++ " , " HTML5 " ] #track list

class listener(StreamListener):
    def on_data(self, data): 
        while True:
            try:
                decoded = json.loads(data)
                msg = ('USER:%s LOCATION:%s TEXT:%s' % (decoded['user']['screen_name'], decoded['user']['location'], decoded['text'].encode('ascii', 'ignore')))
                print(msg)
                print("\n")
                saveFile = open('log2.json', 'a')
                saveFile.write(msg)
                saveFile.write('\n')
                saveFile.close()
                logger.info('found tweet')
                return True
            except BaseException as e:
                print('failed wave,', str(e))
                logger.warning('fail on wave')
                time.sleep(3)
                continue
        exit()
    def on_error(self, status):
        print(status)
>>>>>>> 28142c0c950755f45cc8f851eaf0b7fedff48fb8
		
#OAuth object
auth = OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
<<<<<<< HEAD


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
=======
 
twitterStream = Stream(auth, listener(start_time)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list)  #call the filter method to run the Stream Object
>>>>>>> 28142c0c950755f45cc8f851eaf0b7fedff48fb8
