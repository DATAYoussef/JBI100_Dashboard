import plotly.express as px
import pandas as pd

### Importing cleared dataset from a pickle file ###
def get_data():
    # Read data (has already been processed)
    df = pd.read_pickle('jbi100_app/views/AB_data_withGeo.pickle')

    return df
