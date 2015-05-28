import psycopg2

def start_connection():
	#define connection string that we'll use
	conn_string = "host='localhost' dbname='tweets' user='postgres' password='postgres'"
	print("Connecting to database \n \n ->%s" %(conn_string)

	#connect to (existing) database
	conn = psycopg2.connect(conn_string)

	#open a cursor to perform operation on database (will return a cursor object)
	cursor = conn.cursor()
	print("Connected!\n")

def create_table():
	#execute a command that creates a new table
	cursor.execute("CREATE TABLE tweets (id serial PRIMARY KEY,TIME_STAMP data_tweets, STRING status, STRING location)")

def fill_data():
	# Pass data to fill a query placeholders and let Psycopg perform
	# the correct conversion (no more SQL injections!)
	cursor.execute("INSERT INTO tweets (data_tweets, location, id) VALUES (%s, %s)" ("test", "test", 1))

def select_all():
	cursor.execute("SELECT * FROM tweets;")
	records = cursor.fetchall()

def close_connection():
	conn.commit()

	cursor.close()
	conn.close()

if __name__ in "__main__":
	start_connection()
	create_table()
	fill_data()
	close_connection()
	pprint.pprint(records)

