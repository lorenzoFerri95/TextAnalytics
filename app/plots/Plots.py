
import json
import pandas as pd
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px



def polarity_plot(df, x_col="date", y_col="polarity"):

    fig = px.line(df, x=x_col, y=y_col, title='Polarity Time Series', template="ggplot2")
    
    fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(step="all"),
            dict(count=1, label="1min", step="minute", stepmode="backward"),
            dict(count=1, label="1h", step="hour", stepmode="backward"),
            dict(count=1, label="1d", step="day", stepmode="backward")
            ])
        )
    )

    graphJSON = json.dumps(fig, cls=PlotlyJSONEncoder)
    return graphJSON

