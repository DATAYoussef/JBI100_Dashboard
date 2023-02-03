from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


df = pd.read_pickle('jbi100_app/views/AB_data_withGeo.pickle')


class Scatterplot(html.Div):
    def __init__(self, name, feature_x, feature_y, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = feature_x
        self.feature_y = feature_y

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, selected_color, selected_data):
        self.fig = go.Figure()

        x_values = self.df[self.feature_x]
        y_values = self.df[self.feature_y]
        self.fig.add_trace(go.Scatter(
            x=x_values, 
            y=y_values,
            mode='markers',
            marker_color='rgb(200,200,200)'
        ))
        self.fig.update_traces(mode='markers', marker_size=10)
        self.fig.update_layout(
            yaxis_zeroline=False,
            xaxis_zeroline=False,
            dragmode='select'
        )
        self.fig.update_xaxes(fixedrange=True)
        self.fig.update_yaxes(fixedrange=True)

        # highlight points with selection other graph
        if selected_data is None:
            selected_index = self.df.index  # show all
        else:
            selected_index = [  # show only selected indices
                x.get('pointIndex', None)
                for x in selected_data['points']
            ]

        self.fig.data[0].update(
            selectedpoints=selected_index,

            # color of selected points
            selected=dict(marker=dict(color=selected_color)),

            # color of unselected pts
            unselected=dict(marker=dict(color='rgb(200,200,200)', opacity=0.9))
        )

        # update axis titles
        self.fig.update_layout(
            xaxis_title=self.feature_x,
            yaxis_title=self.feature_y,
        )

        return self.fig

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

    # self.fig.add_trace(go.Scatter(
    #     x=x_values,
    #     y=y_values,
    #     mode='markers',
    #     marker_color='rgb(200,200,200)'
    # ))
    def update(self, selected_attr):
        self.fig = px.choropleth_mapbox(self.df, geojson=self.gjson, color=selected_attr,
                                   locations="fitted_neighbourhood", featureidkey="properties.name",
                                   center={"lat": 40.7, "lon": -74},
                                   mapbox_style="carto-positron",
                                   color_continuous_scale= "Greens",
                                   zoom=9.5, height=750)
        return self.fig


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
        if location =='All Provinces':
            self.fig = px.scatter_mapbox(selected_data, lat="lat", lon="long",
                                         color=self.color,
                                         zoom=10, height=750,
                                         mapbox_style='carto-positron',
                                         hover_data={'lat': False, 'long': False,
                                                     'total_price': True, 'review rate number': True},
                                         color_discrete_sequence=['dark green', 'red', 'light blue', 'grey']
                                         )

            return self.fig
        else:
            self.df = self.df[self.df['neighbourhood group'] == location]

            self.fig = px.scatter_mapbox(self.df, lat="lat", lon="long",
                                    color=self.color,
                                    zoom=10, height=750,
                                    mapbox_style='carto-positron',
                                    color_discrete_sequence=['dark green', 'red', 'light blue', 'grey'],
                                    hover_data={'lat': False, 'long': False,
                                                'total_price': True, 'review rate number': True})

            return self.fig


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
        self.fig =px.line_polar(self.df, r=selected_attr, theta='neighbourhood group', line_close=True,title=selected_attr.capitalize())
        self.fig.update_traces(fill='toself')

        return self.fig


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

    def update(self,location):
        if location == "All Provinces":
            self.fig = px.scatter_matrix(self.df,
            dimensions=["total_price", "availability 365", "review rate number", "calculated host listings count", "number of reviews"],
            color="room type")

            return self.fig

        else:
            self.df = self.df[self.df['neighbourhood group'] == location]

            self.fig = px.scatter_matrix(self.df,
                                         dimensions=["total_price", "availability 365", "review rate number",
                                                     "calculated host listings count", "number of reviews"],
                                         color="room type"
                                         )
            return self.fig