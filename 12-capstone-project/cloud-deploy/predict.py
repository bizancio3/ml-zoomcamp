import pickle
import numpy as np

import pandas as pd 

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

model_path = 'fire1.bin'

#creating instance of fastapi class

app = FastAPI(
    title = "Fire Early Warning API",
    version = 1.0,
    description = "Simple API to assess conditions of potential fire"
)

#loading model

with open(model_path, 'rb') as f_in:
    sc, model = pickle.load(f_in)

#creating API endpoint

@app.post('/predict')
async def predict(payload: Request):
    
    dict = await payload.json()
    
    sample = pd.DataFrame([dict])
    X = sc.transform(sample.to_numpy())
    y_pred = model.predict(X)
   
    if y_pred < 1:
        alarm_code = 'safe'
    elif y_pred < 2:
        alarm_code = 'minor risk'
    elif y_pred < 3:
        alarm_code = 'major risk'
    else:
        alarm_code = 'emergency'

    result = {
        'potential_damage(AREA/ha)': float(np.expm1(y_pred).round(4)),
        'significance': alarm_code
    }

    return JSONResponse(result)

# entrypoint *.py

import os
current_port = int(os.environ.get('PORT'))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=current_port, log_level="info")

