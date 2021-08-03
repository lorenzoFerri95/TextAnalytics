from flask import render_template, request

from app import app

import plotly.express as px
from app.plots.Plots import gdp_plot




@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    description = """
    Prima descrizione
    """
    base_plot = gdp_plot(px.data.gapminder())
    
    
    return render_template('base.html',
                           title = "Page1",
                           header = "Primo Header",
                           graphJSON = base_plot,
                           description = description
                           )

@app.route('/page2')
def page2():
    description = """
    Seconda descrizione
    """
    base_plot = gdp_plot(px.data.gapminder())
    
    
    return render_template('base.html',
                           title = "Page2",
                           header = "Secondo Header",
                           graphJSON = base_plot,
                           description = description
                           )



@app.route('/page1/update-gdp-plot', methods=['POST', 'GET'])
def update_gdp_plot():
    return gdp_plot(px.data.gapminder(), request.args.get('data') )

