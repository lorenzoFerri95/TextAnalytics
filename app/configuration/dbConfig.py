import os
from app import app

app.config["DRIVER"] = os.environ.get('DRIVER') # lettura della variabile d'ambiente specificata
app.config["SERVER"] = os.environ.get('SERVER')
app.config["DATABASE"] = os.environ.get('DATABASE')
app.config["USER"] = os.environ.get('USER')
app.config["PASSWORD"] = os.environ.get('PASSWORD')
app.config["DSN"] = os.environ.get('DSN') # aggiungi un DSN su odbcad32.exe (cercalo sul PC), in "DSN di sistema".
                                            # se usi un DSN servono solo:  USER, PASSWORD, DSN


app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://" + app.config["USER"] + ":" + app.config["PASSWORD"] + "@" + app.config["DSN"]



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