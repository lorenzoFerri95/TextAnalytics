import os
from app import app

app.config["CONSUMER_KEY"] = os.environ.get('CONSUMER_KEY')   # lettura della variabile d'ambiente specificata
app.config["CONSUMER_SECRET"] = os.environ.get('CONSUMER_SECRET')
app.config["ACCESS_TOKEN"] = os.environ.get('ACCESS_TOKEN')
app.config["ACCESS_TOKEN_SECRET"] = os.environ.get('ACCESS_TOKEN_SECRET')

