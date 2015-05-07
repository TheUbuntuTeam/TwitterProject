from twitter import Twitter

# perform a search
twitter_search = Twitter(domain="search.twitter.com")

# Search for the latest News on #python
search = twitter_search.search(q="#python")
for tweet in search['results']:
    print tweet['text']
    print ''

