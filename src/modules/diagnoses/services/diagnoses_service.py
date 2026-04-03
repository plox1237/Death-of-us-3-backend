from fastapi import HTTPException
from sqlmodel import Session
from src.config.database import engine
from src.modules.diagnoses.model.diagnoses_model import Diagnoses
from src.modules.diagnoses.repositories.diagnoses_repository import DiagnosesRepository
from src.shared.utils.pdf_utils import generate_diagnoses_report

diagnoses_repository = DiagnosesRepository(Session(engine))

class DiagnosesService:
    def __init__(self):
        self.repository = diagnoses_repository
    
    async def get_all_diagnoses(self):
        diagnoses = await self.repository.get_all_diagnoses()
        if not diagnoses:
            raise HTTPException(status_code=404, detail="DIAGNOSES NOT FOUND")
        return diagnoses
    
    async def get_diagnosis_by_id(self, diagnosis_id: int):
        diagnosis = await self.repository.get_diagnosis_by_id(diagnosis_id)
        if not diagnosis:
            raise HTTPException(status_code=404,detail="DIAGNOSIS NOT FOUND")
        return diagnosis
    
    async def get_all_diagnoses_by_user_id(self, user_id: int):
        diagnoses = await self.repository.get_all_diagnoses_by_user_id(user_id)
        if not diagnoses:
            raise HTTPException(status_code=404, detail="DIAGNOSES NOT FOUND")
        return diagnoses

    async def get_latest_diagnosis_pdf(self):
        last_diagnoses = await self.repository.get_latest_diagnoses()
        if not last_diagnoses:
            raise HTTPException(status_code=404, detail="DIAGNOSES NOT FOUND")
        formatted = [
            {
                "id": d.diagnosis_id,
                "user_id": d.user_id,
                "user_name": d.user.name,
                "user_last_name": d.user.last_name,
                "pregnancies": d.pregnancies,
                "glucose": d.glucose,
                "blood_pressure": d.blood_pressure,
                "skin_thickness": d.skin_thickness,
                "insulin": d.insulin,
                "bmi": d.bmi,
                "dpf": d.diabetes_pedigree_function,
                "age": d.age,
                "result": "Positivo" if d.result == 1 else "Negativo",
                "probability": round(d.probability * 100, 2)
            }
            for d in last_diagnoses
        ]
        pdf_report = generate_diagnoses_report(formatted)
        return pdf_report
    
    async def create_diagnosis(self, diagnosis: Diagnoses):
        await self.repository.create_diagnosis(diagnosis)
        return
    
    async def delete_diagnosis(self, diagnosis_id: int):
        diagnosis = await self.repository.get_diagnosis_by_id(diagnosis_id)
        if not diagnosis:
            raise HTTPException(status_code=404, detail="DIAGNOSIS NOT FOUND")
        await self.repository.delete_diagnosis(diagnosis)
        return
    