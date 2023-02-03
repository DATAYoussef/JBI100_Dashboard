import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# Everything in cleaning is what we used to clean the data, uncomment it to perform the cleaning

# ################# BEGIN CLEANING
# AB_data = pd.read_csv('data/airbnb_open_data.csv', low_memory=False)  # remove this for descriptive
# original_len = len(AB_data)                                           # remove this for descriptive
# AB_data = AB_data.set_index('id') #not necessary
#
##################################      Remove unused column values
# removed_attributes = ['country', 'country code', 'license',
#                         'house_rules', 'last review', 'reviews per month']
# AB_data = AB_data.drop(removed_attributes, axis=1)
#
# ##################################      Missing observations of non-removed attributes
# AB_data = AB_data[AB_data['price'].notna()]
# AB_data = AB_data[AB_data['service fee'].notna()]
#
# ##################################      Removes $ from price
# AB_data['price'] = AB_data['price'].str[1:]
# AB_data['service fee'] = AB_data['service fee'].str[1:]
#
# ##################################      Some neighbourhood group cleaning (outliers)
# AB_data['neighbourhood group'] = AB_data['neighbourhood group'].replace(['brookln'], 'Brooklyn')
# AB_data['neighbourhood group'] = AB_data['neighbourhood group'].replace(['manhatan'], 'Manhattan')
#
# ##################################      Change price datatype from string to integer
# AB_data['price'] = pd.to_numeric(AB_data['price'].apply(lambda x: x.replace(',','')))
#
# ##################################      Value counts of neighbourhood column
# print(AB_data['neighbourhood'].value_counts())
#
# ##################################      Change service fee datatype from string to integer
# AB_data['service fee'] = pd.to_numeric(AB_data['service fee'].apply(lambda x: x.replace(',','')))
#
# ##################################      Add total price column
# AB_data['total_price'] = AB_data['price'] + AB_data['service fee']
#
# ##################################      Removes missing values (TO BE REVISITED)
# # AB_data_na = AB_data[AB_data.isna().any(axis=1)]
# # print(len(AB_data_na))
# AB_data = AB_data.dropna()
#
# ##################################      Change Construction year, review rate number datatype from float to integer
# print(AB_data.dtypes)
#
# AB_data['Construction year'] = AB_data['Construction year'].astype(np.int64)
# AB_data['review rate number'] = AB_data['review rate number'].astype(np.int64)
# AB_data['number of reviews'] = AB_data['number of reviews'].astype(np.int64)
# AB_data['calculated host listings count'] = AB_data['calculated host listings count'].astype(np.int64)
#
# AB_data['availability 365'] = AB_data['availability 365'].astype(np.int64)
# AB_data['minimum nights'] = AB_data['minimum nights'].astype(np.int64)
#
# ##################################      Remove weird minimum nights and availability 365 values
# AB_data = AB_data[AB_data['minimum nights'] >= 0]
# AB_data = AB_data[(AB_data['availability 365'] >= 0) & (AB_data['availability 365'] <= 365)]
#
#
# ##################################      Missing value analysis
# # print(len(AB_data))
# # print(len(AB_data[(AB_data['availability 365'] < 0) | (AB_data['availability 365'] > 365)])) # 0 because cleaned :)
# # weird_availbility_values = AB_data[(AB_data['availability 365'] < 0) | (AB_data['availability 365'] > 365)]
# # print((len(AB_data) - len(weird_availbility_values)) / original_len)
# # print(len(AB_data[(AB_data['availability 365'] >= 0) & (AB_data['availability 365'] <= 365)]))
#
# ################# END CLEANING

##################################      Adds fitted column (HAS ALL CHANGES FROM ABOVE!!!!!)
AB_data = pd.read_pickle('AB_data_withGeo.pickle')
# print(AB_data['fitted_neighbourhood'].value_counts())


# Everything below is no longer cleaning, only for exploration purposes

##################################      Histogram
# AB_data.hist(column='price', bins=3)
# plt.show()

##################################      Descriptive
# print(AB_data.dtypes)
# print(AB_data.columns)
#
# print(AB_data['instant_bookable'].value_counts(), "\n")
# print(AB_data['cancellation_policy'].value_counts(), "\n")
# print(AB_data['room type'].value_counts(), "\n")
#
# print("Amount of not found neighbourhoods", len(AB_data[AB_data['fitted_neighbourhood'] == 'not found']))
# print("Ratio of not found neighbourhoods", len(AB_data[AB_data['fitted_neighbourhood'] == 'not found']) / len(AB_data))
# print("Original data length:", original_len)
# print("Removed attributes (columns):", removed_attributes)
#
# print("End data length:", len(AB_data))
# print("Data reduction:", (original_len - len(AB_data)) / original_len)

# print(AB_data)

