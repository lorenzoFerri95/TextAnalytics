
from config import TwitterConfig
from tweet_listener import TweetListener
from tweepy import Stream
from tweepy import OAuthHandler

def run_streaming():
    auth = OAuthHandler(TwitterConfig.CONSUMER_KEY, TwitterConfig.CONSUMER_SECRET)
    auth.set_access_token(TwitterConfig.ACCESS_TOKEN, TwitterConfig.ACCESS_TOKEN_SECRET)
    keywords = ["Crypto", "Bitcoin"]
    keywords = [word.strip(' ') for word in keywords]
    listener = TweetListener(keywords)
    stream = Stream(auth, listener)
    stream.filter(track=keywords, languages=['en'])


if __name__ == '__main__':
    run_streaming()