import os

import pandas as pd

import pickle
from sklearn import linear_model as lm

from sklearn.preprocessing import OneHotEncoder, StandardScaler


def prepare_data():
    train = pd.read_csv('data/realty_data.csv', encoding_errors='ignore')
    # train=train.drop(['period','product_name','description','postcode','object_type'], axis=1)
    train = train.drop(['period','product_name','description','postcode','object_type','address_name', 'lat', 'lon', 'source'], axis=1)
    train.city = train.city.fillna('')
    train.rooms = train.rooms.fillna(1)
    train.loc[train['city'] == 'Москва', 'city'] = train['district']
    train.loc[train['city'] == '', 'city'] = train['settlement']
    train = train.drop(['settlement', 'district', 'area'], axis=1)

    ohe = OneHotEncoder()
    res = ohe.fit_transform(train['city'].fillna(value="").to_numpy().reshape(-1, 1))
    ohe_train = pd.DataFrame(res.toarray(), columns=ohe.get_feature_names_out())
    train = pd.concat([train, ohe_train], axis=1).drop(columns='city')

    l=train.columns.to_list()
    del l[0:4]
    l=[x.split('_')[1] for x in l]
    l=[x.replace(' район', '') for x in l]
    l=[x.replace('\xa0', '') for x in l]
    with open('l.pkl', 'wb') as file:
        pickle.dump(l, file)


    return train



def train_model(train):
    from sklearn.ensemble import GradientBoostingRegressor
    X, y = train.drop('price', axis=1), train['price']

    # scaler = StandardScaler()
    # X_scaled = scaler.fit_transform(X)
    gb = GradientBoostingRegressor(random_state=40)

    gb.fit(X, y)

    with open('gb_fitted.pkl', 'wb') as file:
        pickle.dump(gb, file)


def read_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not exists")

    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    return model

