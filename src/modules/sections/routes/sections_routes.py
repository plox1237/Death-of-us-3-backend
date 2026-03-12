from fastapi import APIRouter, Depends
from src.shared.utils.auth_utils import require_section
from src.modules.sections.controllers.sections_controller import SectionsController
from src.modules.sections.model.sections_model import Section

sections_router = APIRouter()
sections_controller = SectionsController()

@sections_router.get("/get_all")
async def get_all_sections(_: dict = Depends(require_section(3))):
    return await sections_controller.get_all_sections()

@sections_router.get("/get_by_id/{section_id}")
async def get_section_by_id(section_id: int, _: dict = Depends(require_section(3))):
    return await sections_controller.get_section_by_id(section_id)

@sections_router.get("/get_by_name/{section_name}")
async def get_section_by_name(section_name: str, _: dict = Depends(require_section(3))):
    return await sections_controller.get_section_by_name(section_name)

@sections_router.post("/create")
async def create_section(section: Section, _: dict = Depends(require_section(3))):
    return await sections_controller.create_section(section)

@sections_router.put("/update/{section_id}")
async def update_section(section_id: int, section: Section, _: dict = Depends(require_section(3))):
    return await sections_controller.update_section(section_id, section)

@sections_router.delete("/delete/{section_id}")
async def delete_section(section_id: int, _: dict = Depends(require_section(3))):
    return await sections_controller.delete_section(section_id)
