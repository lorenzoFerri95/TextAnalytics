
from app import app

#from app.configuration.config import TwitterConfig
from app.services.TweetListenerService import TweetListener
from tweepy import Stream
from tweepy import OAuthHandler

def run_streaming():
    """
    auth = OAuthHandler(TwitterConfig.CONSUMER_KEY, TwitterConfig.CONSUMER_SECRET)
    auth.set_access_token(TwitterConfig.ACCESS_TOKEN, TwitterConfig.ACCESS_TOKEN_SECRET)"""

    auth = OAuthHandler(app.config["CONSUMER_KEY"], app.config["CONSUMER_SECRET"])
    auth.set_access_token(app.config["ACCESS_TOKEN"], app.config["ACCESS_TOKEN_SECRET"])    
    
    keywords = ["Crypto", "Bitcoin"]
    keywords = [word.strip(' ') for word in keywords]
    listener = TweetListener(keywords)
    stream = Stream(auth, listener)
    stream.filter(track=keywords, languages=['en'])