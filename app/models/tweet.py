
from app import db
from datetime import datetime

class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    keyword = db.Column(db.String(256), nullable=False)
    tweet_date = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
    location = db.Column(db.String(100))
    verified_user = db.Column(db.Boolean)
    followers = db.Column(db.Integer)
    sentiment = db.Column(db.Float)

    def __init__(self, body, keyword, tweet_date, location, verified_user, followers, sentiment):
        self.body = body
        self.keyword = keyword
        self.tweet_date = tweet_date
        self.location = location
        self.verified_user = verified_user
        self.followers = followers
        self.sentiment = sentiment

    def __repr__(self):
        return 'Tweet content:  {0}'.format(self.body)