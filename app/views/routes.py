from flask import render_template, request, redirect, url_for

from app import app, db

import pandas as pd
import plotly.express as px
from app.plots.Plots import polarity_plot




@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/polarity')
def polarity():

    data = db.session.execute("""
        SELECT tweet_date, polarity
        FROM tweets
        WHERE polarity <= :lub OR polarity >= :glb
        """,
        {'lub': -0.5,
         'glb': 0.7})
            
    df = pd.DataFrame(data, columns=["date", "polarity"])
    
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index(['date'])
    
    agg_dict = {"polarity": "median"}
    df = df.groupby(df.index.strftime('%Y-%m-%d %H:%M:00')).agg(agg_dict)
    
    df["date"] = df.index
    
    plot = polarity_plot(df)
    
    return render_template('polarity.html',
                           title = "Polarity",
                           header = "Real Time Polarity",
                           graphJSON = plot
                           )


@app.route('/clear_db')
def clear_db():

    db.session.execute("""
        DELETE
        FROM tweets
        """)
    
    db.session.commit()
        
    return redirect(url_for('polarity'))
