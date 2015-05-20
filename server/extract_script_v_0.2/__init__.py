import tweepy
from tweepy import auth
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API


api = tweepy.API(auth)

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

class StdOutListener(tweepy.StreamListener):
	def on_data(self, data):
		# Twitter returns data in JSON format - we need to decode it first
		decoded = json.loads(data)

		# Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
		print ('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
		print ('')
		return True

	def on_error(self, status):
		print (status)
        
        
if __name__ == '__main__':
	listener = StdOutListener()
	#authentication
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	print ("Showing all new tweets for the most famous programming language...")

	stream = tweepy.Stream(auth, listener)
	searched = stream.filter(track=['python -animal' or 'java' or 'go' or 'scala' or 'javascript' or 'php' or 'ruby' or 'cobol' or 'C' or 'C#' or 'Objective C' or 'C++' or 'perl' or 'visualbasic'])

for line in searched:
	new_file = "searched_tweets.txt"
	with open(new_file, 'w') as out:
		out.write(search_result.split())
		out.close()
