from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import os
from dotenv import load_dotenv

"""
il modo migliore di gestire le COSTANTI è metterle in un file  .env  nella root.
questo file poi verrà usato per definire le variabili d'ambiente.

di norma le costanti sono le KEY personali che l'utente deve inserire per far funzionare l'app.
es. connessione al DB, keys degli API ecc...
poiché queste info sono sensibili le nascondiamo a git inserendo .env in .gitignore
mettiamo un file .env.example che fa vedere all'utente come esempio quali variabili deve inserire
"""

load_dotenv()   # cerca il file  .env  nella directory corrente (o in quelle sopra a cascata)
                # e aggiunge le varibili li definite come variabili d'ambiente
                
"""
from app.configuration import twitter_config

from app.configuration import db_config
"""        

             
app.config["CONSUMER_KEY"] = os.environ.get('CONSUMER_KEY')   # lettura della variabile d'ambiente specificata
app.config["CONSUMER_SECRET"] = os.environ.get('CONSUMER_SECRET')
app.config["ACCESS_TOKEN"] = os.environ.get('ACCESS_TOKEN')
app.config["ACCESS_TOKEN_SECRET"] = os.environ.get('ACCESS_TOKEN_SECRET')

app.config["DRIVER"] = os.environ.get('DRIVER')
app.config["SERVER"] = os.environ.get('SERVER')
app.config["DATABASE"] = os.environ.get('DATABASE')
app.config["USER"] = os.environ.get('USER')
app.config["PASSWORD"] = os.environ.get('PASSWORD')
app.config["DSN"] = os.environ.get('DSN') # aggiungi un DSN su odbcad32.exe (cercalo sul PC), in "DSN di sistema".
                                            # se usi un DSN servono solo:  USER, PASSWORD, DSN



app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://" + app.config["USER"] + ":" + app.config["PASSWORD"] + "@" + app.config["DSN"]

db = SQLAlchemy(app)

db.create_all()

from app.controllers import routes