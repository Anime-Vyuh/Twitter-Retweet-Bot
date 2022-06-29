import tweepy
from time import sleep

"""
First copy and paste all the requirement 
"""

API_KEY = "<paste your API key>"
API_KEY_SECRET = "<paste your API key secret>"
ACCESS_TOKEN = "<paste your ACCESS_TOKEN>"
ACCESS_TOKEN_SECRET = "<paste your ACCESS_TOKEN_SECRET>"

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#use api.search_tweets method t
#you can modify the keyword by assigning it to q
#count is the total number of tweets to retrieve or auto retweet
for tweet in api.search_tweets(q="keyword", lang="en",count=60):
    try:
        print("I am In")
        tweet.retweet()
        print('Retweet success')
        sleep(30)
    except Exception as e:
        print(f'Retweet not successful \n Reason:{e}')