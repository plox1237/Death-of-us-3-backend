from src.modules.prediction.prediction.prediction import predict

async def predict_diabetes(data_patient):
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
    return pred, prob