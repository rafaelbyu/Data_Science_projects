from dash import Dash, dcc, html, Input, Output
import pandas as pd
import numpy as np
from sympy import *
from scipy import optimize
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from numpy.polynomial import Chebyshev as T
from numpy.polynomial import Polynomial as P
import scipy.interpolate as si
from tqdm import tqdm




# veldf = pd.read_csv('velocity_slabdata.csv')
#
# velocity = veldf.iloc[:, 0].values
# data_time = pd.to_datetime(veldf.iloc[:, 1], format='%Y-%m-%d %H:%M:%S.%f')
# data_time_int = data_time.astype('int64') // 10 ** 9


# a = np.polynomial.Chebyshev.fit(data_x_int, data_y, 180)
#
# xx, yy = a.linspace(1000)
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
"""Убрал пустые места на графике, иначе интерполяция с ума сходит"""
# df = pd.read_csv("Dataslab/merged_iba_slabdata_2023-08-17_10.csv")
df_1 = pd.read_csv("slab_tracking_script/Data_tracking_csv_fixed_22/slabdataMetrALL_22.csv")


# slab = df.iloc[:, 3]
# data_y_0 = []
# data_x_0 = pd.to_datetime(df.iloc[:, 0], format='%d.%m.%Y %H:%M:%S.%f')


# data_x_int = data_x.astype('int64') // 10 ** 9
# print(data_x)
# data_x_np = np.array(data_x)
# velocity = 0
# slabdata = pd.DataFrame(columns=['velocity', 'current time'])
# data_x_int = data_x.astype('int64') // 10 ** 9
# for i in tqdm(range(1, slab.shape[0])):
#     if slab[i] == 2:
#         data_y_0 = df.iloc[:, 2].values
#     elif slab[i] == 1:
#         data_y_0 = df.iloc[:, 1].values
# data_y_np = np.array(data_y_0)


data_y = df_1.iloc[:, 1]
data_x = pd.to_datetime(df_1.iloc[:, 0], format='%Y-%m-%d %H:%M:%S.%f')
# velocity = df_1.iloc[:, 1]
# data_x_int = data_x.astype('int64') // 10 ** 9


# for i in tqdm(range(10, df.shape[0])):
#     if i%10 == 0 and data_x_int[i]-data_x_int[i-10] != 0:
#         velocity = round((data_y[i]-data_y[i-10])/(data_x_int[i]-data_x_int[i-10]), 6)
#         slabdata = pd.DataFrame([[velocity, data_x[i]]], columns=['velocity', 'current time'])
#         slabdata.to_csv('velocity_slabdata1.csv', mode='a', index=False)

# df_vel = pd.read_csv('velocity_slabdata1.csv')
# velocity_count = df_vel.iloc[:, 0]
# data_x_vel = pd.to_datetime(df_vel.iloc[:, 1], format='%Y-%m-%d %H:%M:%S.%f')

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
        go.Scatter(x=data_x, y=data_y, name="Slab function"),
        row=1, col=1
    )

    # fig.add_trace(
    #     go.Scatter(x=data_x_0, y=data_y_np, name="Slab Iba function"),
    #     row=1, col=1
    # )

    # fig.add_trace(
    #     go.Scatter(x=data_x, y=data_y, name="Slab velocity function"),
    #     row=2, col=1
    # )
    # fig.add_trace(
    #     go.Scatter(x=data_x_vel, y=velocity_count, name="Counted slab velocity function"),
    #     row=2, col=1
    # )

    # fig.add_trace(
    #     go.Scatter(x=xx, y=yy, name="Interpolated human function"),
    # )

    # Set x-axis title
    fig.update_xaxes(title_text="Time")

    # Set y-axes titles
    fig.update_yaxes(
        title_text="Yline",
        secondary_y=False)

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
