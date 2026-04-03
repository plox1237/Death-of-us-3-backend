from fastapi import APIRouter, Depends
from src.modules.prediction.schema.predict_schema import PredictRequest
from src.modules.prediction.controllers.predict_controller import predict_diabetes_controller
from src.shared.utils.auth_utils import require_section

predict_router = APIRouter()

@predict_router.post("/get_predict")
async def get_predict(data_patient: PredictRequest, _: dict = Depends(require_section(2))):
    return await predict_diabetes_controller(data_patient)