"""
import os
from dotenv import load_dotenv



load_dotenv()   # cerca il file  .env  nella directory corrente (o in quelle sopra a cascata)
                # e aggiunge le varibili li definite come variabili d'ambiente


class TwitterConfig:
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')   # lettura della variabile d'ambiente specificata
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


class DBConfig:
    DRIVER = os.environ.get('DRIVER')
    SERVER = os.environ.get('SERVER')
    DATABASE = os.environ.get('DATABASE')
    USER = os.environ.get('USER')
    PASSWORD = os.environ.get('PASSWORD')
    DSN = os.environ.get('DSN') # aggiungi un DSN su odbcad32.exe (cercalo sul PC), in "DSN di sistema".
                                # se usi un DSN servono solo:  USER, PASSWORD, DSN



"""