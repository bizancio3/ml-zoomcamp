#!/usr/bin/env python
# coding: utf-8

import requests

host = 'localhost:8000'
url = f'http://{host}/predict'

sample = {
    "X": 6,
    "Y": 3,
    "FFMC": 91.1,
    "DMC": 141.1,
    "DC": 629.1,
    "ISI": 7.1,
    "temp": 19.3,
    "RH": 39,
    "wind": 3.6,
    "rain": 0
}

response = requests.post(url, json=sample).json()
print(response)

