#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

from xgboost.sklearn import XGBClassifier



# training 
best_parameters = {
    'min_child_weight': 3, 
    'max_depth': 8, 
    'learning_rate': 0.15
    }

def train(df_train, y_train): 
    dicts = df_train.to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = XGBClassifier()
    model.fit(X_train, y_train)
    
    return dv, model


def predict(df, dv, model):
    dicts = df.to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred


# Save the model
output_file = 'water1.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')
