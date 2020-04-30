import pandas as pd
import numpy as np
from pymongo import MongoClient

client = MongoClient('mongodb://root:rootpassword@wine-db:27017/sommelier')
database = client['sommelier']
collection_wine = database['wine']

#TODO: Get connection from secrets
def csv_to_json(filename, header=None):
    data = pd.read_csv(filename, header=header)
    data = data.drop([
        data.columns[0],
        'region_1',
        'winery',
        'region_2',
        'designation',
        'taster_name',
        'taster_twitter_handle',
        'province'
    ], axis = 1).replace(
        np.nan, '', regex=True
    ).drop_duplicates(
        subset='title', keep="first"
    )
    data['price'] = pd.to_numeric(data['price'],errors='coerce')

    return data.to_dict('records')

collection_wine.insert_many(
    csv_to_json('./dataset/wine-review.csv', 0)
)
