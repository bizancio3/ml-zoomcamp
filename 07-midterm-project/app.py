import pickle

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
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

#data schema for input parameters
class Input(BaseModel):
    ph:float
    hardness:float
    solids:float
    chloramines:float
    sulfate:float
    conductivity:float
    organic_carbon:float
    trihalomethanes:float
    turbidity:float

#creating endpoint
@app.post("/",tags = ["predict"])
def predict(features:Input):
    sample = features.dict()
    
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
