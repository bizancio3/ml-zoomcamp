import pickle

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

model_path = 'water1.bin'
threshold = 0.5

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
    safety = (y_pred >= threshold)

    result = {
        'water_potability': float(y_pred),
        'safety': bool(safety)
    }

    return JSONResponse(result)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="info")
