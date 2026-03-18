from fastapi import HTTPException
from sqlmodel import Session
from src.config.database import engine
from src.modules.diagnoses.model.diagnoses_model import Diagnoses
from src.modules.diagnoses.repositories.diagnoses_repository import DiagnosesRepository

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
    
    async def create_diagnosis(self, diagnosis: Diagnoses):
        await self.repository.create_diagnosis(diagnosis)
        return
    
    async def delete_diagnosis(self, diagnosis_id: int):
        diagnosis = await self.repository.get_diagnosis_by_id(diagnosis_id)
        if not diagnosis:
            raise HTTPException(status_code=404, detail="DIAGNOSIS NOT FOUND")
        await self.repository.delete_diagnosis(diagnosis)
        return
    