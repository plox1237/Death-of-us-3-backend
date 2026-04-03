from sqlmodel import Session
from src.config.database import engine
from src.modules.prediction.prediction.prediction import predict
from src.modules.prediction.schema.predict_schema import PredictRequest
from src.modules.diagnoses.model.diagnoses_model import Diagnoses
from src.modules.diagnoses.repositories.diagnoses_repository import DiagnosesRepository

diagnoses_repository = DiagnosesRepository(Session(engine))

async def predict_diabetes(data_patient: PredictRequest):
    data = [
        data_patient.pregnancies,
        data_patient.glucose,
        data_patient.blood_pressure,
        data_patient.skin_thickness,
        data_patient.insulin,
        data_patient.bmi,
        data_patient.diabetes_pedigree_function,
        data_patient.age
    ]
    pred, prob = predict(data)
    pred = int(pred.flatten()[0])
    prob = float(prob.flatten()[0])
    diagnosis = Diagnoses(
        user_id=data_patient.user_id,
        pregnancies=data_patient.pregnancies,
        glucose=data_patient.glucose,
        blood_pressure=data_patient.blood_pressure,
        skin_thickness=data_patient.skin_thickness,
        insulin=data_patient.insulin,
        bmi=data_patient.bmi,
        diabetes_pedigree_function=data_patient.diabetes_pedigree_function,
        age=data_patient.age,
        result=pred,
        probability=prob
    )
    await diagnoses_repository.create_diagnosis(diagnosis)
    return pred, prob