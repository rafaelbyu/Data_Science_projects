from dash import Dash, dcc, html, Input, Output
import pandas as pd
import numpy as np

from plotly.subplots import make_subplots
import plotly.graph_objects as go




# def plot_graph(file):
#     df = pd.read_csv(file)
#     data_x = pd.to_datetime(df['Time'], format='%Y-%m-%d %H:%M:%S.%f')
#     data_x = data_x.astype('int64') // 10 ** 9
#     data_x = data_x - 1690502400
#     data_y = df['Human'].values
#     app = Dash(__name__)
#
#     a, b, c, d, e, f, g, k, l, m, n, o, p, = polyfit(data_x, data_y, 12)
#     y_pred = np.polyval([a, b, c, d, e, f, g, k, l, m, n, o, p], data_x)
#
#     graph = dcc.Graph(
#         id='graph',
#         figure={
#             'data': [{
#                 'Time': data_x, 'Human': data_y, 'type': 'line', 'name': 'Original function'
#             },
#                 {'Time': data_x, 'Human': y_pred, 'type': 'line', 'name': 'Interpolated function'
#             }],
#             'layout': {'title': 'Графики функции'}
#         }
#     )
#
#     app.layout = html.Div(
#         children=[
#             html.H4("Simple stock plot with adjustable axis"),
#             graph
#         ]
#     )
#
#     # @app.callback(
#     #     Output("graph", "figure"),
#     #     Input("button", "n_clicks"),
#     # )
#     # def display_graph(n_clicks):
#     #         x, y = data_x, "Human"
#     #         fig1 = px.line(df, x=x, y=y)
#     #         fig2 = px.line(df, x=x, y=y)
#     #         return fig1, fig2
#
#     if __name__ == "__main__":
#         app.run_server(debug=True)

df = pd.read_csv("data.csv")

data_x = df.iloc[:, 0]

data_y = df.iloc[:, 1]
print(data_x)

a = np.polynomial.Chebyshev.fit(data_x, data_y, 255)

xx, yy = a.linspace(1000)


app = Dash(__name__)

app.layout = html.Div([
    html.H4('Interactive data-scaling function and interpolated function'),
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
        go.Scatter(x=data_x, y=data_y, name="function"),
    )

    fig.add_trace(
        go.Scatter(x=xx, y=yy, name="Interpolated function"),
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Index")

    # Set y-axes titles
    fig.update_yaxes(
        title_text="Value",
        secondary_y=False)

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
