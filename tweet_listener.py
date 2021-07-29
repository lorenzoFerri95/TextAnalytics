from db_connection import session_scope, engine
from models.base import Base

from models.tweet import Tweet
from tweepy.streaming import StreamListener
import logging
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

logger = logging.getLogger(__name__)



class TweetListener(StreamListener):

    def __init__(self, keywords):
        
        StreamListener.__init__(self)
        
        Base.metadata.create_all(bind=engine)   # crea le tabelle definite nei  models  se esse non esistono
        
        self.keywords = keywords
        self.sentiment_model = SentimentIntensityAnalyzer()  # o  TextBlob()

    def on_status(self, status):
        """metodo chiamato quando arriva un nuovo Tweet, i cui dati vengono storati in  status"""
        
        if status.retweeted or 'RT @' in status.text:
            return  # se il tweet è un retweet non facciamo nulla (lo saltiamo, altrimenti lo duplicheremmo nel DB)
        
        # quando un tweet eccede una certa lughezza limite (truncated tweet)
        # il suo testo viene salvato in un attributo speciale (status.extended_tweet)
        # altrimenti è salvato semplicemente in  status.text
        if status.truncated:
            text = status.extended_tweet['full_text']
        else:
            text = status.text
        
        location = status.coordinates
        if location:
            location = str(status.coordinates['coordinates'])   # otteniamo la location string se presente
        
        keyword = self.check_keyword(text)  # checkiamo la keyword
        if not keyword:
            return
        
        sentiment = self.sentiment_model.polarity_scores(text).get('compound')  # calcoliamo il sentiment score
        if sentiment == 0:
            return  # se il sentiment è 0 non inseriamo il tweet perché altrimenti la grande maggioranza sarebbero tutti 0
        
        tweet = Tweet(body=text, keyword=keyword, tweet_date=status.created_at, location=location,
                      verified_user=status.user.verified, followers=status.user.followers_count,
                      sentiment=sentiment)
        self.insert_tweet(tweet)

    def on_error(self, status_code):
        """metodo chiamato quando c'è un errore, che viene restituito nello  status_code"""
        if status_code == 420:
            # Stream limit reached, need to close the stream
            logger.warning('Limit Reached. Closing stream ({})'.format(self.keywords))
            return False
        logger.warning('Streaming error (status code {})'.format(status_code))

    def insert_tweet(self, tweet):
        """inserisce il tweet nel DB usando la sessione definita in  db_connection"""
        try:
            with session_scope() as sess:
                sess.add(tweet) # aggiungiamo il tweet
        except Exception as e:
            logger.warning('Unable to insert tweet: {}'.format(e))

    def check_keyword(self, body):
        """checka quale keyword è presente nel tweet, in modo da inserirla nel DB"""
        for keyword in self.keywords:
            if keyword in body:
                return keyword
        return None