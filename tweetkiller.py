#!/usr/bin/python/

'''
Copyright 2016 Tiffany B. Brown

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import csv, json, twitter

# First, download your Twitter archive 
# <https://support.twitter.com/articles/20170160?lang=en>. 
# Expand that ZIP file and update the line below with the
# path to the tweets.csv file.
# This file contains the identifiers for every tweet you've posted.

PATH_TO_TWEETS = ''

# Next, create a Twitter app. <https://apps.twitter.com/>
# That's how you'll get your keys and secrets

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Delete tweets before this date in YYYY-MM-DD format
BEFORE_DATE = False

###### Stop editing

# Deletes the tweet matching the tweetid passed.
# Requires you to be authenticated
def deletetweet(tweetid):
    try:
        deletedobj = twitterapi.DestroyStatus(tweetid)
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
            
            print deleted
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
