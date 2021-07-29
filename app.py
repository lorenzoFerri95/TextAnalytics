from flask import Flask, render_template, request
import plotly.express as px
from models.plots.GDP import gdp

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    header="Primo Header"
    description = """
    Prima descrizione
    """
    base_plot = gdp(px.data.gapminder())
    
    
    return render_template('base.html',
                           title = "Page1",
                           header = header,
                           graphJSON = base_plot,
                           description = description
                           )

@app.route('/page2')
def page2():
    header="Secondo Header"
    description = """
    Seconda descrizione
    """
    base_plot = gdp(px.data.gapminder())
    
    
    return render_template('base.html',
                           title = "Page2",
                           header = header,
                           graphJSON = base_plot,
                           description = description
                           )



@app.route('/page1/update-gdp-plot', methods=['POST', 'GET'])
def update_gdp_plot():
    return gdp(px.data.gapminder(), request.args.get('data') )



if __name__ == "__main__":
    app.run(debug=True)