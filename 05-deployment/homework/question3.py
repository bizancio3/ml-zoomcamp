#!/usr/bin/env python
# coding: utf-8

import pickle

customer = {
    "contract": "two_year",
    "tenure": 12,
    "monthlycharges": 19.7
}

model_file = 'model1.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


def predict():

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    print(round(float(y_pred), 4), bool(churn))
 
    return y_pred, churn
    

if __name__ == "__main__":
    predict()
    

