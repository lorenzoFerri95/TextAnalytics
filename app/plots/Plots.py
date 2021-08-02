
import json
import pandas as pd
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px


def gdp_plot(data, country='Italy'):
    df = pd.DataFrame(data)

    fig = px.line(df[df['country']==country], x="year", y="gdpPercap")

    graphJSON = json.dumps(fig, cls=PlotlyJSONEncoder)
    return graphJSON