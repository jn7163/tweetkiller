# tweetkiller

WIP Python application that deletes your tweets

- Requires Python 3 (Built with 3.5.2)

# How to use

1. **Download your [Twitter Archive](https://support.twitter.com/articles/20170160?lang=en).** This will provide a comma-delimited text file with an identifier for each tweet we want to delete.
1. **Create a [Twitter app](https://apps.twitter.com/)**. This is how you get your Consumer Key, Consumer Secret, Access Token, and Access Token Secret.
1. **Clone this repo.** 
1. **Update `tweetkillerconf.py`** with the keys and secrets generated in step 1.


## What this does

It does exactly what [Twitter](https://support.twitter.com/articles/18906) says happens when you delete a tweet.

- Removes tweets from your account
- Removes retweets of your tweet

But be aware that:

- Twitter may still retain copies of your Tweet in its database.
- Third parties, such as [the Wayback Machine](https://archive.org/web/) and the Library of Congress, still have archives of your tweets. 