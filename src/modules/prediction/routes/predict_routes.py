from fastapi import APIRouter
from src.modules.prediction.schema.predict_schema import PredictRequest
from src.modules.prediction.controllers.predict_controller import predict_diabetes_controller

predict_router = APIRouter()

@predict_router.post("/get_predict")
async def get_predict(data_patient: PredictRequest):
    return await predict_diabetes_controller(data_patient)