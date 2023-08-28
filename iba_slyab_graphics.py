import numpy as np
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv(
    "new_merged.csv"
)

df2 = pd.read_csv(
    ""
)


xx = pd.to_datetime(df2[''], format='%Y-%m-%d %H:%M:%S.%f')
yy = df2['ylist'].values
data_xx = xx.astype('int64') // 10 ** 9

data_x = df.iloc[:, 0]
data_x = pd.to_datetime(df.iloc[:, 0], format='%d.%m.%Y %H:%M:%S.%f')
# data_x = data_x.astype('int64') // 10 ** 9

# data_x_np = np.array(data_x)

data_y = df.iloc[:, 1]

dy_dx_slab = np.gradient(yy, data_xx)

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Interactive data-scaling iba function and slabdata function'),
    dcc.RadioItems(
        id='radio',
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"),
    Input("radio", "value"))
def display_(radio_value):

    # Create figure with secondary y-axis
    fig = make_subplots()

    # Add traces
    fig.add_trace(
        go.Scatter(x=data_x, y=data_y, name=""),
    )

    fig.add_trace(
        go.Scatter(x=xx, y=yy, name=""),
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Time")

    # Set y-axes titles
    fig.update_yaxes(
        title_text="Distance",
        )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
