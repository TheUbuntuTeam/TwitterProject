def save_tweets(tweets):
    conn = psycopg2.connect(host='localhost',
                            port=5432,
                            dbname='lesson_10',
                            user='test_10',
                            password='test_10')
    curs = conn.cursor()
    for tweet in tweets:
        curs.execute(
            'INSERT INTO tweets2 (id, date, text) VALUES (%s, %s, %s)',
            (tweet['id'], tweet['created_at'], tweet['text'])
        )
    curs.close()
    conn.commit()
    conn.close()