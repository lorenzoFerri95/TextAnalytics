import os
from app import app

app.config["DRIVER"] = os.environ.get('DRIVER')
app.config["SERVER"] = os.environ.get('SERVER')
app.config["DATABASE"] = os.environ.get('DATABASE')
app.config["USER"] = os.environ.get('USER')
app.config["PASSWORD"] = os.environ.get('PASSWORD')
app.config["DSN"] = os.environ.get('DSN') # aggiungi un DSN su odbcad32.exe (cercalo sul PC), in "DSN di sistema".
                                            # se usi un DSN servono solo:  USER, PASSWORD, DSN






"""
from sqlalchemy import create_engine
from config import DBConfig

from sqlalchemy.orm import scoped_session, sessionmaker
from contextlib import contextmanager

# usiamo il DSN per creare la connessione con il DB
engine = create_engine("mssql+pyodbc://" + DBConfig.USER + ":" + DBConfig.PASSWORD + "@" + DBConfig.DSN)
"""


""" altrimenti avremmo potuto specificare la stringa di connessione intera
from sqlalchemy.engine import URL
connection_string = "DRIVER=" + DBConfig.DRIVER + ";\
                    SERVER=" + DBConfig.SERVER + ";\
                    DATABASE=" + DBConfig.DATABASE + ";\
                    UID=user" + DBConfig.USER + ";\
                    PWD=" + DBConfig.PASSWORD

connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
"""
"""
# definiamo una sessione di connessione al DB, una per ogni tweet processato
DBSession = scoped_session(sessionmaker(autocommit=False, bind=engine))

@contextmanager # questo decoratore permette di creare un oggetto di sessione che può essere usato con la sintassi  with ... as ...
def session_scope():
    session = DBSession()
    try:
        yield session
        session.commit()    # se non ci sono errori si committa
    except:
        session.rollback()  # se c'è un errore si elimina l'ultima sessione (rollback)
        raise
    finally:
        session.close()     # in ognuno dei casi precedenti la connessione viene sempre chiusa, per ogni tweet
"""