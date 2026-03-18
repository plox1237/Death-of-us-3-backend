from fastapi import APIRouter
from src.shared.utils.auth_utils import require_section
from src.modules.diagnoses.model.diagnoses_model import Diagnoses
from src.modules.diagnoses.controllers.diagnoses_controller import DiagnosesController

diagnoses_router = APIRouter()
diagnoses_controller = DiagnosesController()

@diagnoses_router.get("/get_all")
async def get_all_diagnoses():
    return await diagnoses_controller.get_all_diagnoses()

@diagnoses_router.get("/get_by_id/{diagnosis_id}")
async def get_diagnosis_by_id(diagnosis_id: int):
    return await diagnoses_controller.get_diagnosis_by_id(diagnosis_id)

@diagnoses_router.get("/get_by_user/{user_id}")
async def get_all_diagnoses_by_user_id(user_id: int):
    return await diagnoses_controller.get_all_diagnoses_by_user_id(user_id)

@diagnoses_router.post("/create")
async def create_diagnosis(diagnosis: Diagnoses):
    return await diagnoses_controller.create_diagnosis(diagnosis)

@diagnoses_router.delete("/delete/{diagnosis_id}")
async def delete_diagnosis(diagnosis_id: int):
    return await diagnoses_controller.delete_diagnosis(diagnosis_id)