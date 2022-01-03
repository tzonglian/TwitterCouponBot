import tweepy
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# auth=tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('SECRET'))
# auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

client=tweepy.Client(bearer_token=None, consumer_key=os.getenv('CONSUMER_KEY'), consumer_secret=os.getenv('SECRET'), access_token=os.getenv('ACCESS_TOKEN'), access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))

def publictweet():
    if datetime.date.today().weekday() == 0:
        tweettopublish = 'Hi everyone, today is Monday.   #Monday '
    if datetime.date.today().weekday() == 1:
        tweettopublish = 'Enjoy your Tuesday.  #Tuesday'
    if datetime.date.today().weekday() == 2:
        tweettopublish = 'Third week of the Week. #Wednesday'
    if datetime.date.today().weekday() == 3:
        tweettopublish = 'Thursday. I cannot wait for the Weekend'
    if datetime.date.today().weekday() == 4:
        tweettopublish = 'Friday...Finally'
    if datetime.date.today().weekday() == 5:
        tweettopublish = 'Great it is Saturday #weekend #Saturday'
    if datetime.date.today().weekday() == 6:
        tweettopublish = 'Sunday morning...#Weekend #enjoy '   
        
    client.create_tweet(text=tweettopublish)
    print(tweettopublish)
publictweet()