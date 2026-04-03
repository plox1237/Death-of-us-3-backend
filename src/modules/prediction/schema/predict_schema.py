from pydantic import BaseModel

class PredictRequest(BaseModel):
    user_id: int
    pregnancies: int
    glucose: int
    blood_pressure: int
    skin_thickness: int
    insulin: int
    bmi: float
    diabetes_pedigree_function: float
    age: int