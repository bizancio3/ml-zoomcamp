#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

from catboost import CatBoostClassifier

output_file = 'water1.bin'
random_seed = 42

# ETL

df_raw = pd.read_csv("water_potability.csv")
df_raw.columns = df_raw.columns.str.lower()

def fill_nan(df):
    for index, column in enumerate(df.columns[:9]):
        df[column] = df[column].fillna(df.groupby('potability')[column].transform('mean'))
    
    return df
        
df = fill_nan(df_raw)

# fulltrain, test datasets
 
X = df.drop(['potability'], axis = 1)
y = df['potability']                                       

X_fulltrain, X_test, y_fulltrain, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)

# scaling
sc = StandardScaler()
X_fulltrain = sc.fit_transform(X_fulltrain)
X_test = sc.transform(X_test)

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

# Save model as binary

with open(output_file, 'wb') as f_out:
    pickle.dump((sc, model), f_out)

print(f'the model is saved to {output_file}')
