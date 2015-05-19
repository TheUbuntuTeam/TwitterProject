import requests
import base64
import psycopg2
def save_tweets2():
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        dbname='twitter_db')
    curs = conn.cursor()
    #for tweet in tweets:
    curs.execute(
        'INSERT INTO tweets (id_tweet, data_tweet, testo, location) VALUES (%s, %s, %s, %s)',
        ('10', '2012-5-5 00:00:00', 'IL LINGUAGGIO CHE MI PIACE DI PIU E JAVA!!!', 'Fiume Veneto')
    )
    conn.commit()
    conn.close()

def save_tweets3():
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        dbname='twitter_db')
    curs = conn.cursor()
    #for tweet in tweets:
    curs.execute(
        'INSERT INTO tweets (id_tweet, data_tweet, testo, location) VALUES (%s, %s, %s, %s)',
        ('10', '2015-5-5 00:00:00', 'IL LINGUAGGIO CHE MI PIACE DI PIU E C#!!!', 'Pordenone')
    )
    conn.commit()
    conn.close()


