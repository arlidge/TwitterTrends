import json
import tweepy

from credentials import *
import ast
woeid = input('woeid ')
file_path = input('Save file as anything.json ')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

trend = api.trends_place(woeid)

print(json.dumps(trend,sort_keys=True,indent=4))
with open(file_path, 'w') as outfile:
    json.dump(trend, outfile,indent=4, sort_keys=True)
