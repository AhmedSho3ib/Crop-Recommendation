from fastapi import FastAPI, HTTPException
from utils.FactorsData import FactorsData
from utils.config import APP_NAME, VERSION, encoder_preprocessor, scaler_preprocessor, logistic_regression_model, random_forest_model
from utils.inference import predict_new

app = FastAPI(title=APP_NAME, version=VERSION)

@app.get('/', tags=['General'])
async def home():
    return {"message": f'Welcome to {APP_NAME}, version {VERSION}'}


@app.post('/predict/forest', tags=['Models'])
def forest_predict(data:FactorsData) -> dict:
    try:
        result = predict_new(data=data, preprocessor=scaler_preprocessor, label_encoder=encoder_preprocessor, model=random_forest_model)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/predict/logistic', tags=['Models'])
def logistic_reg_predict(data:FactorsData) -> dict:
    try:
        result = predict_new(data=data, preprocessor=scaler_preprocessor, label_encoder=encoder_preprocessor, model=logistic_regression_model)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


