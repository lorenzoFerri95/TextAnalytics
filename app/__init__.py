from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from app.configuration import config


db = SQLAlchemy(app)

from app.models.tweet import Tweet
db.create_all()

from app.views import routes