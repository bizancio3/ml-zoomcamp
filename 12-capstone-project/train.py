#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor

import pickle
import sklearn.metrics as metrics

# input settings 

path = './input/forestfires.csv'

output_file = 'fire1.bin'
seed = 101
split_ratio = 0.3

# ETL pipeline

forestfire = pd.read_csv(path)    

forestfire['arealog'] = np.log1p(forestfire.area)

y = forestfire['arealog'].to_numpy()
X = forestfire.drop(
    columns=['arealog', 'area', 'month', 'day']
    ).to_numpy()                            

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=split_ratio, 
    random_state=seed, 
    shuffle=True
    )

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# optimal hyperparamenters

best_param = {
    'n_neighbors': 43, 
    'weights': 'uniform'
    }

# model training 

model = KNeighborsRegressor(**best_param)

model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print()
print('Goodness of model adjustment')
print('Model: KNeighborsRegressor')
print('--------------------------------------')
print('Explained variance: ', 
    round(metrics.explained_variance_score(y_test, y_pred), 4)
    )    
print('Coef. determination r2: ', 
    round(metrics.r2_score(y_test, y_pred),4)
    )
print('Mean absolute error (MAE): ', 
    round(metrics.mean_absolute_error(y_test, y_pred),4)
    )
print('Root mean square error (RMSE): ', 
    round(np.sqrt(metrics.mean_squared_error(y_test, y_pred)),4)
    )
print()

# exporting model as binary

with open(output_file, 'wb') as f_out:
    pickle.dump((sc, model), f_out)

print(f'KNeighborsRegressor saved to {output_file}')
print()