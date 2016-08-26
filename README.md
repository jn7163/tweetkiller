# tweetkiller

Python script that deletes your tweets &#8212; either all of them, or only ones before a particular date.

- Requires Python 3 (Developed with 3.5.2)
- [`python-twitter` 3.1+](https://pypi.python.org/pypi/python-twitter/3.1) 

You can install `python-twitter` and its dependencies using PIP.

```bash
pip install -r requirements.txt
```
Consider installing and using [`virtualenv`](https://pypi.python.org/pypi/virtualenv) for running this script.

```bash
pip install virtualenv
```
Note that you may need to use `sudo` with this command.

## How to use

1. **Download your [Twitter Archive](https://support.twitter.com/articles/20170160?lang=en).** This will provide a comma-delimited text file with an identifier for each tweet we want to delete.

1. **Create a [Twitter app](https://apps.twitter.com/)**. This is how you get your Consumer Key, Consumer Secret, Access Token, and Access Token Secret.

1. **Clone this repo.**

1. **Create a virtual environment with virtualenv.** For example, `virtualenv deletemytweets`. Then start the environment using `source deletemytweets/bin/activate`.

1. **Rename `tweetkillerconf.sample.py` to `tweetkillerconf.py` and update it** with the keys and secrets provided by Twitter in Step 2.

1. **Set the `BEFORE_DATE`** to delete only those tweets  posted before a certain date. Set to `False` _if you want to delete **all** of your tweets_. 

  I can't stress this enough: **If you do not set a date, you will delete ALL of your tweets**
1. **Open a terminal window, and run this script** using `python tweetkiller/tweetkiller.py`. Note that you may have to adjust the permissions of `tweetkiller.py` and/or its parent directory in order to run it.

## What this does

It does exactly what [Twitter](https://support.twitter.com/articles/18906) says happens when you delete a tweet.

- Removes tweets from your public timeline.
- Removes retweets of your tweet.

Be aware that:

- Twitter may still retain copies of your Tweet in its database.
- Third parties, such as [the Wayback Machine](https://archive.org/web/) and the United States Library of Congress, may still have archives of your tweets.
- It _will not_ remove your retweets of other users' tweets. You'll have to undo those retweets separately. (Currently, this script does not do that.)

## Disclaimer, no warranties, no support

This is a hastily-written-in-an-afternoon project by a Python n00b. There is no test suite. There are probably bugs. It will delete things. It might delete things you didn't want it to delete. Test yourself with a small batch of tweets. It comes with no promises or warranties about its fitness for a particular purpose. _I also do not provide technical support._


 
