
from app import db
from datetime import datetime

class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    keyword = db.Column(db.String(256), nullable=False)
    tweet_date = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
    verified_user = db.Column(db.Boolean)
    followers = db.Column(db.Integer)
    polarity = db.Column(db.Float)
    
    def __repr__(self):
        return 'Tweet text:  {0}'.format(self.body)