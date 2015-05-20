from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#change the path when you have stored the credentials
credentials = open('/home/marco/project_work/TwitterProject/.credentials', 'r')

def reader():
	for line in credentials.read().splitlines():
		yield line

keys = reader()
consumer_key = keys.__next__()
consumer_secret = keys.__next__()
access_token = keys.__next__();
access_token_secret = keys.__next__()
credentials.close()

class Listener(StreamListener):
 
	def on_data(self, data):
		print (data)
		return True


	def on_error(self, status):	
		print (status)

#got authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#got stream
stream = Stream(auth, Listener())
stream.filter(track=["PYTHON" or "JAVA" or "PHP" or "JAVASCRIPT" or "RUBY" or "COBOL" or "C" or "C#" or "OBJECTIVE C" or "C++" or "ASSEMBLY" or "PERL" or "SCALA" or "GO" or "VISUALBASIC"])
