#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import classification_report

from catboost import CatBoostClassifier

# parameters
output_file = 'water1.bin'
random_seed = 42

# ETL pipeline
df_raw = pd.read_csv("water_potability.csv")
df_raw.columns = df_raw.columns.str.lower()

def fill_nan(df):
    for index, column in enumerate(df.columns[:9]):
        df[column] = df[column].fillna(df.groupby('potability')[column].transform('mean'))
    
    return df
df = fill_nan(df_raw)

# split fulltrain, test
X = df.drop(['potability'], axis = 1)
y = df['potability']                                       

df_fulltrain, df_test, y_fulltrain, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)

tempdict_1 = df_fulltrain.to_dict(orient='records')
tempdict_2 = df_test.to_dict(orient='records')

dv = DictVectorizer(sparse=False)

X_fulltrain = dv.fit_transform(tempdict_1)
X_test = dv.transform(tempdict_2)

# training 
params = {
    'loss_function' : 'Logloss',
    'eval_metric' : 'AUC',
    'verbose' : 200,
    'random_seed' : random_seed
}

model = CatBoostClassifier(**params)

model.fit(
    X_fulltrain, y_fulltrain,
    eval_set=(X_test, y_test),
    use_best_model=True,
    plot=True
)

y_pred = model.predict(X_test)

print()
print(classification_report(y_test, y_pred))

# Save model as binary

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'Catboost model is saved to {output_file}')
