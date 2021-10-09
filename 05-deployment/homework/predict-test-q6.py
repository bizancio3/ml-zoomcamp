#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

customer_id = 'question6'
customer = {
    "contract": "two_year", 
    "tenure": 12, 
    "monthlycharges": 10
}


response = requests.post(url, json=customer).json()
print(response)
