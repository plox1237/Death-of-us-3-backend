from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.encoders import jsonable_encoder
from src.modules.diagnoses.model.diagnoses_model import Diagnoses
from src.modules.diagnoses.services.diagnoses_service import DiagnosesService

diagnoses_service = DiagnosesService()

class DiagnosesController:
    def __init__(self):
        self.service = diagnoses_service
    
    async def get_all_diagnoses(self):
        try:
            diagnoses = await self.service.get_all_diagnoses()
            data = jsonable_encoder(diagnoses)
            return JSONResponse(content={
                "message": "DIAGNOSES FOUND",
                "data": data
            }, status_code=200)
        except Exception as e:
            print("ERROR GETTING DIAGNOSES: ", e)
            raise e
        
    async def get_diagnosis_by_id(self, diagnosis_id: int):
        try:
            diagnosis = await self.service.get_diagnosis_by_id(diagnosis_id)
            data = jsonable_encoder(diagnosis)
            return JSONResponse(content={
                "message": "DIAGNOSIS FOUND",
                "data": data
            }, status_code=200)
        except Exception as e:
            print("ERROR GETTING DIAGNOSIS: ", e)
            raise e
    
    async def get_all_diagnoses_by_user_id(self, user_id: int):
        try:
            diagnoses = await self.service.get_all_diagnoses_by_user_id(user_id)
            data = jsonable_encoder(diagnoses)
            return JSONResponse(content={
                "message": "DIAGNOSES FOUND",
                "data": data
            }, status_code=200)
        except Exception as e:
            print("ERROR GETTING DIAGNOSES BY USER ID: ", e)
            raise e
    
    async def get_latest_diagnoses_pdf(self):
        try:
            pdf_buffer = await self.service.get_latest_diagnosis_pdf()
            return StreamingResponse(
                pdf_buffer,
                media_type="application/pdf",
                headers={
                    "Content-Disposition": "attachment; filename=latest_diagnoses_report.pdf"
                }
            )
        except Exception as e:
            print("ERROR GETTING LATEST DIAGNOSES PDF: ", e)
            raise e
    
    async def create_diagnosis(self, diagnosis: Diagnoses):
        try:
            await self.service.create_diagnosis(diagnosis)
            return JSONResponse(content={
                "message": "DIAGNOSIS CREATED"
            }, status_code=201)
        except Exception as e:
            print("ERROR CREATING DIAGNOSIS \n", e)
            raise e
        
    async def delete_diagnosis(self, diagnosis_id: int):
        try:
            await self.service.delete_diagnosis(diagnosis_id)
            return JSONResponse(content={
                "message": "DIAGNOSIS DELETED",
            }, status_code=200)
        except Exception as e:
            print("ERROR DELETING DIAGNOSIS \n", e)
            raise e
