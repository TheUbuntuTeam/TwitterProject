import requests
import base64
import psycopg2
def save_tweets2():
    connDB = psycopg2.connect(host='localhost',
                            port=5432,
                            dbname='twitter_db',
                            user='ubuntuteam',
                            password='UbuntuTeam')
    curs = connDB.cursor()
    #for tweet in tweets:
    curs.execute(
        'INSERT INTO tweets (id_tweet, data_tweet, testo, location) VALUES (%s, %s, %s, %s)',
        ('10', '2012-5-5 00:00:00', 'IL LINGUAGGIO CHE MI PIACE DI PIU E JAVA!!!', 'Lignano')
    )
    connDB.commit()
    connDB.close()

def save_tweets3():
    connDB = psycopg2.connect(host='localhost',
                            port=5432,
                            dbname='twitter_db',
                            user='ubuntuteam',
                            password='UbuntuTeam')
    curs = connDB.cursor()
   # for tweet in tweets3:
    curs.execute(
            'INSERT INTO tweets (id_tweet, data_tweet, testo, location) VALUES (%s, %s, %s, %s)',
            ('10', '2015-5-5 00:00:00', 'IL LINGUAGGIO CHE MI PIACE DI PIU E C#!!!', 'Udine')
            )
    connDB.commit()
    connDB.close()

def save_tweets(tweets):
    conn = psycopg2.connect(host='localhost',
                            port=5432,
                            dbname='twitter_db',
                            user='ubuntuTeam',
                            password='Password!')
    curs = conn.cursor()
    for tweet in tweets:
        curs.execute(
            'INSERT INTO tweets2 (id, data_tweet, testo, location) VALUES (%s, %s, %s,%s)',
            (tweet['id'], tweet['created_at'], tweet['text'], tweet['text'])
        )
    conn.commit()
    conn.close()

save_tweets3()
save_tweets2()