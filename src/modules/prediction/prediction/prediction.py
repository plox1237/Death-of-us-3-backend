import joblib
import numpy as np

model = joblib.load("modelo_diabetes.pkl")
scaler = joblib.load("scaler.pkl")

def predict(data_patient):
    data = np.array([data_patient])
    data = scaler.transform(data)
    pred = model.predict(data)
    prob = model.predict_proba(data)
    return pred, prob