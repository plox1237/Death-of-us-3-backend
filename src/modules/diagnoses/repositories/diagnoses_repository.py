from sqlmodel import select, Session
from src.modules.diagnoses.model.diagnoses_model import Diagnoses

class DiagnosesRepository:
    def __init__(self, session: Session):
        self.session = session
    
    async def get_all_diagnoses(self):
        try:
            statement = select(Diagnoses).order_by(Diagnoses.diagnosis_id)
            results = self.session.exec(statement).all()
            return results
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def get_diagnosis_by_id(self, diagnosis_id: int):
        try: 
            statement = select(Diagnoses).where(Diagnoses.diagnosis_id == diagnosis_id)
            result = self.session.exec(statement).first()
            return result
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def get_all_diagnoses_by_user_id(self, user_id: int):
        try:
            statement = select(Diagnoses).where(Diagnoses.user_id == user_id).order_by(Diagnoses.diagnosis_id)
            result = self.session.exec(statement).all()
            return result
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def get_latest_diagnoses(self):
        try:
            statement = select(Diagnoses).order_by(Diagnoses.diagnosis_id.desc()).limit(10)
            result = self.session.exec(statement).all()
            return result
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def create_diagnosis(self, diagnosis: Diagnoses):
        try:
            self.session.add(diagnosis)
            self.session.commit()
            self.session.refresh(diagnosis)
        except Exception as e:
            self.session.rollback()
            raise e

    async def delete_diagnosis(self, diagnosis: Diagnoses):
        try:
            self.session.delete(diagnosis)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
