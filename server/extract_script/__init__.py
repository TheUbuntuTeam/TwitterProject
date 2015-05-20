import requests
import base64
import psycopg2
#import Twitter



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
	
	
HEAD
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
	f_destination = open("tweets.txt", "w") 
	i = 1
	for tweet in tweets:
		f_destination.write('{} {}'.format(i, tweet))
		i += 1
	f_destination.close()
=======
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
    
def save_cleared_tweets(tweets):
    f_destination = open("tweetsCL.txt", "w")
    i = 1
    for tweet in tweets:
        try:
            str = '{} {} {} {}'.format(i, tweet['id'], tweet['text'], tweet['retweet_count'])
            f_destination.write(str + '\n')
            i += 1
        except UnicodeEncodeError:
            pass
    f_destination.close()
>>>>>>> 9c4745b2671c1054863c623856d13a1a08b3364e


if __name__ == '__main__':
	
    import os
    import sys
    print('getting token...')
    token = get_token(
        os.environ['TWITTER_APP_ID'],
        os.environ['TWITTER_APP_SECRET'])
    print('getting tweets...')
    tweets = search_tweets(sys.argv[1], token)
    print('saving tweets...')
    save_tweets(tweets)
    print('OK!')
    save_cleared_tweets(tweets)
    print('clearing ok')
