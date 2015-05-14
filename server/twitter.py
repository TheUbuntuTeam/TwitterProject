from twitter import TwitterStream, UserPassAuth, Twitter

# put a file twitter-pwd.txt with your 
# username and password in differnt lines
with open('twitter-pwd.txt','r') as f:
    lines = f.read().splitlines()
    username = lines[0].strip()
    password = lines[1].strip()

# open stream
twitter_stream = TwitterStream(auth=UserPassAuth(username,password))

# print stream
for tweet in twitter_stream.statuses.sample():
    if 'delete' in tweet: continue # skip deleted
    print tweet['user']['screen_name']
    print '    ', tweet['text']
    print ''



from twitter import TwitterStream, UserPassAuth, Twitter

# put a file twitter-pwd.txt with your 
# username and password in differnt lines
with open('twitter-pwd.txt','r') as f:
    lines = f.read().splitlines()
    username = lines[0].strip()
    password = lines[1].strip()

# open stream
twitter_stream = TwitterStream(auth=UserPassAuth(username,password))

# print stream
for tweet in twitter_stream.statuses.sample():
    if 'delete' in tweet: continue # skip deleted
    print tweet['user']['screen_name']
    print '    ', tweet['text']
    print ''