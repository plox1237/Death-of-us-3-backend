from fastapi.responses import JSONResponse
from src.modules.prediction.services.predict_service import predict_diabetes

async def predict_diabetes_controller(data_patient):
    try:
        pred, prob = await predict_diabetes(data_patient)
        return JSONResponse(status_code=200, content={
            "message": "PREDICTION SUCCESS",
            "prediction": pred.tolist(), 
            "probability": prob.tolist()
            })
    except Exception as e:
        print("ERROR DURING PREDICTION: \n", e)
        return JSONResponse(status_code=500, content={
            "message": "PREDICTION FAILED",
            "error": str(e)
            })
