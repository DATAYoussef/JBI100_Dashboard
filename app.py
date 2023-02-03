from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.scatterplot import Scatterplot, ChoroplethMapbox,Scatter_geo,Radarplot,SPLOM

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

    # preperation for radar plot:
    grouped_province = df.groupby(['neighbourhood group']).agg(
        {'total_price': 'mean', 'availability 365': 'mean', 'minimum nights': 'mean',
         "review rate number": 'mean'})
    grouped_province = grouped_province.reset_index()

    ### plots ##
    chloropleth = ChoroplethMapbox("ChoroplethMapbox Price", df_grouped, geojson)
    scattergeo = Scatter_geo("Scattergeo Price", df, "room type", "review rate number")
    radarplot = Radarplot('Radar Plot',grouped_province,'total_price')
    splom = SPLOM('SPLOM', df, 'room type')



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
                    chloropleth,
                    scattergeo,
                    radarplot,
                    splom
                ],
            ),
        ],
    )


    ### CHLOROPLETH INTERACTION ###
    @app.callback(
        Output(chloropleth.html_id, "figure"), [
        Input("select-attribute-chloro", "value")
    ])
    def update_scatter_1(selected_attr):
        return chloropleth.update(selected_attr)


    ### SCATTERGEO INTERACTION ###
    @app.callback(
        Output(scattergeo.html_id, "figure"), [
        Input("select-province-scattergeo", "value"),
    ])
    def update_scatter_2(location):
        if location == 'All Provinces':
            return scattergeo.update(location, df)
        else:
            df_scatter = df[df['neighbourhood group'] == location]
            return scattergeo.update(location, df_scatter)

    ### RADAR INTERACTION ###
    @app.callback(
        Output(radarplot.html_id, "figure"), [
        Input("select-attribute-radar", "value"),
        ])
    def update_radar(province):
        return radarplot.update(province)


    ### SPLOM INTERACTION ###
    @app.callback(
        Output(splom.html_id, "figure"),[
        Input("select-province-splom","value"),
        ])
    def update_splom(location):
        return splom.update(location)

    app.run_server(debug=False, dev_tools_ui=False)