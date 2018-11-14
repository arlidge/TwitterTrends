import json
import tweepy

from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

trend = api.trends_available()

print(json.dumps(trend,sort_keys=True,indent=4))
with open('data.json', 'w') as outfile:
    json.dump(trend, outfile,indent=4, sort_keys=True)
