import requests
import base64
import psycopg2
#import Twitter

#query = "https://api.twitter.com/1.1/search/tweets.json?q=%23python -animal %3A)&src=typd"
#localized_query = 

def get_token(client_id, client_secret):
    credentials = '{}:{}'.format(client_id, client_secret)
    credentials_b64 = base64.b64encode(credentials.encode())
    resp = requests.post(
        'https://api.twitter.com/oauth2/token',
        headers={
            'Authorization': 'Basic {}'.format(credentials_b64.decode())
        },
        data={'grant_type': 'client_credentials'}
    )
    if resp.status_code == 200:
        data = resp.json()
        return data['access_token']
    else:
        raise ValueError(
            'error in request, code={} body={}'.format(resp.status_code, resp.text)
        )

def search_tweets(what, token):
	url = 'https://api.twitter.com/1.1/search/tweets.json'
	resp = requests.get(
	url,
	headers = {'Authorization': 'Bearer {}'.format(token)},
	params={'q': what, 'lang': 'it'}
	)
	resp.raise_for_status()
	data = resp.json()
	return data['statuses']
	
	
#if __name__ == "main":
#	get_token()


#~ def save_tweets(tweets):
    #~ conn = psycopg2.connect(host='localhost',
                            #~ port=5432,
                            #~ dbname='twitter_db',
                            #~ user='UbuntuTeam',
                            #~ password='Password!')
    #~ curs = conn.cursor()
    #~ for tweet in tweets:
        #~ curs.execute(
            #~ 'INSERT INTO tweets2 (id, date, text) VALUES (%s, %s, %s)',
            #~ (tweet['id'], tweet['created_at'], tweet['text'])
        #~ )
    #~ conn.commit()
    #~ conn.close()
 
def save_tweets(tweets):
    conn = psycopg2.connect(host='localhost',
                            port=5432,
                            dbname='twitter_db',
                            user='UbuntuTeam',
                            password='Password!')
    curs = conn.cursor()
    for tweet in tweets:
        curs.execute(
            'INSERT INTO tweets2 (id, date, text) VALUES (%s, %s, %s)',
            (tweet['id'], tweet['created_at'], tweet['text'])
        )
    conn.commit()
    conn.close()
    
#~ def save_tweets(tweets):
	#~ f_destination = open("tweets.txt", "w") 
	#~ i = 1
	#~ for tweet in tweets:
		#~ f_destination.write('{} {}'.format(i, tweet))
		#~ i += 1
	#~ f_destination.close()


#if __name__ == '__main__':
	
#	import os
#	import sys
#	print('getting token...')
#	token = get_token(
#		os.environ['TWITTER_APP_ID'],
 #       os.environ['TWITTER_APP_SECRET']
#	)
#	print('getting tweets...')
#	tweets = search_tweets(sys.argv[1], token)
#	print('saving tweets...')
#	save_tweets(tweets)
#	print('OK!')	
#