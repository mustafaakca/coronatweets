<<<<<<< HEAD
import tweepy
import datetime
import xlsxwriter
import sys

#My Twitter Account Information

#the real values are hidden
consumer_key = ""
consumer_secret = ""
access_token = "1"
access_token_secret = ""

#Collect all the tweets in a list
tweets = []

#windows
#dsdsdsa

#date filter
start="2020-04-01"
end= "2020-04-02"
#startDate = datetime.datetime(2020, 4, 1, 0, 0, 0)
#endDate =   datetime.datetime(2020, 4, 15, 0, 0, 0)

# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

# Continue with rest of code
#Another alternative to tweepy, tweepy could give more results and more feautare but we can
#only use it for the last week tweets. 

#Informarion for Old Tweets https://pypi.org/project/GetOldTweets3/
#https://github.com/Jefferson-Henrique/GetOldTweets-python

#Information for tweepy 
#https://bhaskarvk.github.io/2015/01/how-to-use-twitters-search-rest-api-most-effectively./
#https://gist.github.com/alexdeloy/fdb36ad251f70855d5d6
# https://readthedocs.org/projects/tweepy/downloads/pdf/latest/

import GetOldTweets3 as got

queries = ['corona vefat',  'corona öldü' , 'coronadan vefat' , 'coronadan öldü', 'coronavirus vefat','coronavirus öldü']

workbook = xlsxwriter.Workbook('tweetsaboutdeaths' + ".xlsx")
worksheet = workbook.add_worksheet('ff')
row = 0
for query in queries:

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query)\
                                           .setSince(start)\
                                           .setUntil(end)\
                                           .setMaxTweets(100000)

    for tweet in got.manager.TweetManager.getTweets(tweetCriteria):
        worksheet.write_string(row, 0, str(tweet.id))
        worksheet.write_string(row, 1, str(tweet.date))
        worksheet.write(row, 2, tweet.text)
        worksheet.write(row, 3,query)
       # worksheet.write_string(row, 3, str(tweet.geo ))
        row += 1


=======
import tweepy
import datetime
import xlsxwriter
import sys

#My Twitter Account Information

#the real values are hidden
consumer_key = ""
consumer_secret = ""
access_token = "1"
access_token_secret = ""

#Collect all the tweets in a list
tweets = []


start="2020-04-01"
end= "2020-04-02"
#startDate = datetime.datetime(2020, 4, 1, 0, 0, 0)
#endDate =   datetime.datetime(2020, 4, 15, 0, 0, 0)

# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

# Continue with rest of code
#Another alternative to tweepy, tweepy could give more results and more feautare but we can
#only use it for the last week tweets. 

#Informarion for Old Tweets https://pypi.org/project/GetOldTweets3/
#https://github.com/Jefferson-Henrique/GetOldTweets-python

#Information for tweepy 
#https://bhaskarvk.github.io/2015/01/how-to-use-twitters-search-rest-api-most-effectively./
#https://gist.github.com/alexdeloy/fdb36ad251f70855d5d6
# https://readthedocs.org/projects/tweepy/downloads/pdf/latest/

import GetOldTweets3 as got

queries = ['corona vefat',  'corona öldü' , 'coronadan vefat' , 'coronadan öldü', 'coronavirus vefat','coronavirus öldü']

workbook = xlsxwriter.Workbook('tweetsaboutdeaths' + ".xlsx")
worksheet = workbook.add_worksheet('ff')
row = 0
for query in queries:

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query)\
                                           .setSince(start)\
                                           .setUntil(end)\
                                           .setMaxTweets(100000)

    for tweet in got.manager.TweetManager.getTweets(tweetCriteria):
        worksheet.write_string(row, 0, str(tweet.id))
        worksheet.write_string(row, 1, str(tweet.date))
        worksheet.write(row, 2, tweet.text)
        worksheet.write(row, 3,query)
       # worksheet.write_string(row, 3, str(tweet.geo ))
        row += 1


>>>>>>> 98f844f62c08086864c53e82f7ca8ae95d16e3fa
workbook.close()