import pickle

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

model_path = 'water1.bin'
# reminder:
# include threshold for water safety as parameter

#creating the app (instance of fastapi object)
app = FastAPI(
    title = "Water Potability API",
    version = 1.0,
    description = "Simple API to predict safety of drinking water"
)

#loading best model
with open(model_path, 'rb') as f_in:
    dv, model = pickle.load(f_in)

#creating endpoint
@app.post('/predict')
async def predict(payload: Request):
    sample = await payload.json()
    
    X = dv.transform([sample])
    y_pred = model.predict_proba(X)[0, 1]
    safety = y_pred >= 0.5

    result = {
        'water_potability': float(y_pred),
        'safety': bool(safety)
    }

    return JSONResponse(result)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
