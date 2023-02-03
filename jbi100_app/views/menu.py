from dash import dcc, html
from ..config import color_list1, color_list2,provinces,attributes

options2 = [{"label": i, "value": i} for i in provinces]
radar_attr = ['total_price', 'availability 365', 'minimum nights', "review rate number"]
radar_labels = [
    {'label': 'Total price', 'value': 'total_price'},
    {'label': 'Availability', 'value': 'availability 365'},
    {'label': 'Minimum nights', 'value': 'minimum nights'},
    {'label': 'Review rate', 'value': 'review rate number'}
]
choro_labels = [
    {'label': 'Total price', 'value': 'total_price'},
    {'label': 'Availability', 'value': 'availability 365'},
    {'label': 'Minimum nights', 'value': 'minimum nights'},
    {'label': 'Host listings', 'value': 'calculated host listings count'},
    {'label': 'Number of reviews', 'value': 'number of reviews'},
    {'label': 'Review rate', 'value': 'review rate number'}
]

def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
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
    return html.Div(
        id="control-card",
        children=[
            html.Label("ChoroplethMap Attribute"),
            dcc.Dropdown(
                id="select-attribute-chloro",
                options=choro_labels,
                value=attributes[0],
            ),
            html.Br(),
            html.Label("Scattergeo Neighbourhood group"),
            dcc.Dropdown(
                id="select-province-scattergeo",
                options=[{"label": i, "value": i} for i in provinces],
                value=provinces[0],
            ),
            html.Br(),
            html.Label("Radar Attribute"),
            dcc.Dropdown(
                id="select-attribute-radar",
                options=radar_labels,
                value=radar_attr[0],
            ),
            html.Br(),
            html.Label("SPLOM Neighbourhood group"),
            dcc.Dropdown(
                id="select-province-splom",
                options=[{"label": i, "value": i} for i in provinces],
                value=provinces[0],
            )

        ], style={"textAlign": "float-left"}
    )


def make_menu_layout():
    return [generate_description_card(), generate_control_card()]
