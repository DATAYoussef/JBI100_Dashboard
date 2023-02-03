import plotly.express as px
import pandas as pd


def get_data():
    # Read data
    df = pd.read_pickle('jbi100_app/views/AB_data_withGeo.pickle')

    # Any further data preprocessing can go her

    return df
