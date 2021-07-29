from flask import Flask, render_template, request
import pandas as pd
import json
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px

app = Flask(__name__)

@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))
   
@app.route('/')
def index():
    return render_template('index.html',  graphJSON=gm())

def gm(country='Italy'):
    df = pd.DataFrame(px.data.gapminder())

    fig = px.line(df[df['country']==country], x="year", y="gdpPercap")

    graphJSON = json.dumps(fig, cls=PlotlyJSONEncoder)
    return graphJSON


if __name__ == "__main__":
    app.run(debug=True)