from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import jbi100_app.data as data


### Importing dataset for plots that are using default dataframe ###
df = data.get_data()



### Class to plot ChoroplethMap ###
class ChoroplethMapbox(html.Div):
    def __init__(self, name, df, gjson, feature_x=0, feature_y=0):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.gjson = gjson
        self.feature_x = feature_x
        self.feature_y = feature_y

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id)
            ],
        )


    def update(self, selected_attr):
        self.fig = px.choropleth_mapbox(self.df, geojson=self.gjson, color=selected_attr,
                                   locations="fitted_neighbourhood", featureidkey="properties.name",
                                   center={"lat": 40.7, "lon": -74},
                                   mapbox_style="carto-positron",
                                   color_continuous_scale= "Greens",
                                   labels={
                                    "total_price": "Total price",
                                    "availability 365": "Availability",
                                    "review rate number": "Review rate",
                                    "minimum nights": "Minimum nights",
                                    "number of reviews": "Number of reviews",
                                    "calculated host listings count": "Host listings count"
                                   },
                                   zoom=9.5, height=750)
        return self.fig


### Class to plot ScatterGeo ###
class Scatter_geo(html.Div):
    def __init__(self,name,df,color,size):
        self.html_id = name.lower().replace(" ", "-")
        self.color = color
        self.size = size
        self.df = df



        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id)
            ],)

    def update(self,location = "All Provinces", selected_data = df):
        self.fig = px.scatter_mapbox(selected_data, lat="lat", lon="long",
                                     color=self.color,
                                     zoom=10, height=750,
                                     mapbox_style='carto-positron',
                                     hover_data={'lat': False, 'long': False,
                                                 'total_price': True, 'review rate number': True},
                                     color_discrete_sequence=['dark green', 'red', 'light blue', 'grey']
                                         )

        return self.fig


### Class to plot Radar Plot ###
class Radarplot(html.Div):
    def __init__(self,name,df,column,theta = 'neighbourhood group',):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.column = column
        self.theta = theta

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id)
            ],
        )


    def update(self,selected_attr):
        self.fig =px.line_polar(self.df, r=selected_attr, theta='neighbourhood group', line_close=True,title=selected_attr.capitalize().replace('_', ' '))
        self.fig.update_traces(fill='toself')

        return self.fig


### Class to plot SPLOM ###
class SPLOM(html.Div):
    def __init__(self,name,df,color):
        self.html_id = name.lower().replace(" ", "-")
        self.color = color
        self.df = df

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id)
            ], )


    def update(self,location,selected_data):

        self.fig = px.scatter_matrix(selected_data,
                                     dimensions=["total_price", "availability 365","review rate number",
                                                 "calculated host listings count", "number of reviews"],
                                     color="room type",
                                     height=800,
                                     labels={
                                         "number of reviews": "# of reviews",
                                         "calculated host listings count": "host listings count",
                                         "review rate number": "review rate"
                                     }
                                     )
        self.fig.update_traces(diagonal_visible = False)
        self.fig.update_yaxes(tickangle=-45)
        return self.fig

