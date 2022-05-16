from secrets import *
import tweepy, json, os , requests , random
myfile = "mytweets.txt"
Myuser_mentions = "user_mentions.txt"
My_user_id = "1255125948908912643"


def make_tweet(what_to_tweet):
    my_tweets_from_app = open(myfile,"a")
    my_tweets_from_app.write(what_to_tweet)
    my_tweets_from_app.close()
    
    try :
        client = tweepy.Client(bearer_token=B_token)
        client.access_token = A_TOKEN
        client.access_token_secret= A_TOKEN_SECRET
        client.consumer_key= C_KEY
        client.consumer_secret=C_SECRET
        client.create_tweet(text=what_to_tweet)   
    except Exception as E :
        print(E)
    
make_tweet('Real Madrid survive superb Chelsea comeback to reach Champions League semis ')
