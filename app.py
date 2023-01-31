from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.scatterplot import Scatterplot, ChoroplethMapbox,Scatter_geo

import pandas as pd
import json

from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output


if __name__ == '__main__':
    # Create data
    df_iris = px.data.iris()
    df = pd.read_pickle('jbi100_app/views/AB_data_withGeo.pickle')

    # BEGIN
    with open("jbi100_app/views/nyc-neighborhoods.geo.json", "r") as geojsonfile:
        geojson = json.load(geojsonfile)

    df_grouped = df.groupby(['fitted_neighbourhood']).mean()
    df_grouped = df_grouped.reset_index()

    # print(AB_data)
    # print(geojson)
    # print(AB_grouped)



    scatterplot1 = ChoroplethMapbox("ChoroplethMapbox Price", df_grouped, geojson)

    # Instantiate custom views
    scatterplot2 = Scatter_geo("Scattergeo Price",df,"room type","review rate number")

    # preperation for radar plot:
    grouped_province = df.groupby(['neighbourhood group']).agg(
        {'total_price': 'mean', 'availability 365': 'mean', 'instant_bookable': 'count', 'minimum nights': 'mean',
         "review rate number": 'mean'})
    instant_bookable = {}
    for key, item in grouped_province:
        true = len(item[item['instant_bookable'] == True])
        ratio = (true / len(item)) * 100
        print(true, ratio)
        instant_bookable[key] = ratio




    app.layout = html.Div(
        id="app-container",
        children=[
            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=make_menu_layout()
            ),

            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children=[
                    scatterplot1,
                    scatterplot2
                ],
            ),
        ],
    )

    # Define interactions
    @app.callback(
        Output(scatterplot1.html_id, "figure"), [
        Input("select-attribute-chloro", "value"),
        Input(scatterplot2.html_id, 'selectedData')
    ])
    def update_scatter_1(selected_attr, selected_data):
        return scatterplot1.update(selected_attr, selected_data,)

    @app.callback(
        Output(scatterplot2.html_id, "figure"), [
        Input("select-province-scattergeo", "value"),
        Input(scatterplot1.html_id, 'selectedData')
    ])
    def update_scatter_2(location,selected_data):
        return scatterplot2.update(location,selected_data)


    app.run_server(debug=False, dev_tools_ui=False)