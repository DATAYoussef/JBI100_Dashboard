from dash import dcc, html
from ..config import provinces,attributes,radar_attr,radar_labels,choro_labels

def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    ### Adding Heading and intro for Upper Left Column ###
    return html.Div(
        id="description-card",
        children=[
            html.H5("NYC AirBnB Analysis"),
            html.Div(
                id="intro",
                children="Welcome to our dashboard! We're group 69 from the JBI100 Visualization course. Our goal is to increase AirBnB host profitability."
            ),
        ],
    )


def generate_control_card():
    """

    :return: A Div containing controls for graphs.
    """
    ### Adding Dropdown Menus on Left Column ###

    return html.Div(
        id="control-card",
        children=[
            html.Label("ChoroplethMap Attributes"),
            dcc.Dropdown(
                id="select-attribute-chloro",
                options=choro_labels,
                value=attributes[0],
            ),
            html.Br(),
            html.Label("Scattergeo Provinces"),
            dcc.Dropdown(
                id="select-province-scattergeo",
                options=[{"label": i, "value": i} for i in provinces],
                value=provinces[0],
            ),
            html.Br(),
            html.Label("Radar Attributes"),
            dcc.Dropdown(
                id="select-attribute-radar",
                options=radar_labels,
                value=radar_attr[0],
            ),
            html.Br(),
            html.Label("SPLOM Provinces"),
            dcc.Dropdown(
                id="select-province-splom",
                options=[{"label": i, "value": i} for i in provinces],
                value=provinces[0],
            )

        ], style={"textAlign": "float-left"}
    )


def make_menu_layout():
    return [generate_description_card(), generate_control_card()]
