from dash import dcc, html
from ..config import color_list1, color_list2,provinces,attributes

options2 = [{"label": i, "value": i} for i in provinces]
radar_attr = ['total_price', 'availability 365', 'minimum nights', "review rate number"]

# options2[0] = {'label': 'All provinces', "value": True}


def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("JBI100-Group 69 Dashboard"),
            html.Div(
                id="intro",
                children="You can use dropdowns for changing the plots",
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
            html.Label("ChoroplethMapbox Select Attribute"),
            dcc.Dropdown(
                id="select-attribute-chloro",
                options=[{"label": i, "value": i} for i in attributes],
                value=attributes[0],
            ),
            html.Br(),
            html.Label("Scattergeo Change Province"),
            dcc.Dropdown(
                id="select-province-scattergeo",
                options=[{"label": i, "value": i} for i in provinces],
                value=provinces[0],
            ),
            html.Br(),
            html.Label("Radar Change Attribute"),
            dcc.Dropdown(
                id="select-attribute-radar",
                options=[{"label": i, "value": i} for i in radar_attr],
                value=radar_attr[0],
            )
        ], style={"textAlign": "float-left"}
    )


def make_menu_layout():
    return [generate_description_card(), generate_control_card()]
