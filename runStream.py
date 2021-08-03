from app import app
from app.services.TweetListenerService import TweetListener
from tweepy import OAuthHandler
from tweepy import Stream

def run_streaming(keywords):
    
    keywords = [word.strip(' ') for word in keywords]
    listener = TweetListener(keywords)
    
    twitterAuth = OAuthHandler(app.config["CONSUMER_KEY"], app.config["CONSUMER_SECRET"])
    twitterAuth.set_access_token(app.config["ACCESS_TOKEN"], app.config["ACCESS_TOKEN_SECRET"]) 

    stream = Stream(twitterAuth, listener)
    stream.filter(track=keywords, languages=['en'])


if __name__ == "__main__":

    run_streaming(keywords = ["Crypto", "Bitcoin"])
