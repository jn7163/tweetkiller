#!/usr/bin/env python

import csv
import json
import twitter

from conf import PATH_TO_TWEETS
from conf import CONSUMER_KEY, CONSUMER_SECRET
from conf import ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from conf import BEFORE_DATE

# Deletes the tweet matching the tweetid passed.
# Requires you to be authenticated
def deletetweet(tweetid):
    try:
        deletedobj = twitterapi.DestroyStatus(tweetid)
        return tweetid
    except:
        return False
# END deletetweet

# Compares two dates
def isbefore(basedate, dateinquestion):
    return dateinquestion < basedate
# END isbefore


# Deletes a tweet if it's before a particular date
def deletetweetifbefore(tweetid, tweettime, beforedate):
    if isbefore(beforedate, tweettime):
        return deletetweet(tweetid)
# END deletetweetifbefore


def deletetweets(pathtotweets, beforedatecutoff = ''):
    with open(pathtotweets) as tweetfile:
        tweets = csv.DictReader(tweetfile)
        
        for row in tweets:
            if beforedatecutoff:
                deleted = deletetweetifbefore(row['tweet_id'], row['timestamp'], beforedatecutoff)
            else:
                deleted = deletetweet(row['tweet_id'])
            print("Tweet {} was deleted".format(deleted))
# End deletetweets    

# Initializes an API object
twitterapi = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

# Authenticates you (or not if your tokens are wrong / disabled)
try:
    authenticated = twitterapi.VerifyCredentials()
except:
    print("Your API keys, secrets, or tokens are either wrong or disabled.")

deletetweets(PATH_TO_TWEETS, BEFORE_DATE)

