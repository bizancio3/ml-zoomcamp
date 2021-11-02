#!/usr/bin/env python
# coding: utf-8

import requests

host = 'localhost:8000'
url = f'http://{host}/predict'

sample = {
    "ph": 7.1,
    "hardness": 225,
    "solids": 22000,
    "chloramines": 8.5,
    "sulfate": 377,
    "conductivity": 290,
    "organic_carbon": 11.5,
    "trihalometanes": 70,
    "turbidity": 4
}

response = requests.post(url, json=sample).json()
print(response)

if response['safety'] == True:
    print('water sample is safe to drink')
else:
    print('water is not safe for human consumption')