#!/usr/bin/python/

import csv, json, twitter

''' 
First, download your Twitter archive 
<https://support.twitter.com/articles/20170160?lang=en>. 
Expand that ZIP file and update the line below with the
path to that file.
''' 

PATH_TO_TWEETS = ''

'''
Next, create a Twitter app. <https://apps.twitter.com/>
That's how you'll get your keys and secrets
'''

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

MESSAGES = {
	'success' : 'Successfully deleted http://twitter/{0}/status/{1}.',
	'error' : 'Looks like tweet {0} was already deleted.'
}

# Deletes the tweet and prints a message.
# Requires you to be authenticated
def deletetweet(tweetid, messageobject, uname):
	if(twitterapi):
		try:
			deletedobj = twitterapi.DestroyStatus(tweetid)
		except:
			print(messageobject['error'].format(tweetid))
		print(messageobject['success'].format(uname, tweetid))
	
			
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

with open(PATH_TO_TWEETS) as tweetfile:
	tweets = csv.DictReader(tweetfile)
	for row in tweets:
		deletetweet(row['tweet_id'], MESSAGES, authenticated.screen_name)
		
