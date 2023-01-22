from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.scatterplot import Scatterplot, ChoroplethMapbox

import pandas as pd
import json

from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output


if __name__ == '__main__':
    # Create data
    df = pd.read_pickle('jbi100_app/views/AB_data_withGeo.pickle')

    # BEGIN
    with open("jbi100_app/views/nyc-neighborhoods.geo.json", "r") as geojsonfile:
        geojson = json.load(geojsonfile)

    df_grouped = df.groupby(['fitted_neighbourhood']).mean()
    df_grouped = df_grouped.reset_index()

    # print(AB_data)
    # print(geojson)
    # print(AB_grouped)

    # attributes = ["total_price", "availability 365", "review rate number", "minimum nights",
    #               "calculated host listings count", "Construction year", "number of reviews"]
    # for attr in attributes:
    scatterplot1 = ChoroplethMapbox("ChoroplethMapbox Price", df_grouped, geojson)
    # scatterplot1.show()
    # END

    # Instantiate custom views
    # scatterplot1 = Scatterplot("Scatterplot 1", 'sepal_length', 'sepal_width', df)
    scatterplot2 = Scatterplot("Scatterplot 2", 'petal_length', 'petal_width', df)

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
        Input("select-color-scatter-1", "value"),
        Input(scatterplot2.html_id, 'selectedData')
    ])
    def update_scatter_1(selected_color, selected_data):
        return scatterplot1.update(selected_color, selected_data)

    @app.callback(
        Output(scatterplot2.html_id, "figure"), [
        Input("select-color-scatter-2", "value"),
        Input(scatterplot1.html_id, 'selectedData')
    ])
    def update_scatter_2(selected_color, selected_data):
        return scatterplot2.update(selected_color, selected_data)


    app.run_server(debug=False, dev_tools_ui=False)