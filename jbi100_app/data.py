import plotly.express as px
import pandas as pd


def get_data():
    # Read data
    df = pd.read_pickle('AB_data_withGeo.pickle')

    # Any further data preprocessing can go her

    return df
