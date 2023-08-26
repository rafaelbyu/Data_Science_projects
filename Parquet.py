from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import pyarrow


def plot_graph(file):
    df = pd.read_parquet(file)
    app = Dash(__name__)

    app.layout = html.Div(
        [
            html.H4("Simple stock plot with adjustable axis"),
            html.Button("Switch Axis", n_clicks=0, id="button"),
            dcc.Graph(id="graph"),
        ]
    )

    @app.callback(
        Output("graph", "figure"),
        Input("button", "n_clicks"),
    )
    def display_graph(n_clicks):
            x, y = "current time", "velocity"
            fig = px.line(df, x=x, y=y)
            return fig

    if __name__ == "__main__":
        app.run_server(debug=True)


file = "my_new_parquet.parquet"
plot_graph(file)
