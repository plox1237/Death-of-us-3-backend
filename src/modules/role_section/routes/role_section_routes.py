from fastapi import APIRouter, Depends
from src.modules.role_section.model.role_section_model import RoleSection
from src.modules.role_section.controllers.role_section_controller import RoleSectionController
from src.modules.auth.dependencies.auth_dependencies import get_current_user

role_section_router = APIRouter()
role_section_controller = RoleSectionController()

@role_section_router.get("/get_all")
async def get_all_role_sections(_: dict = Depends(get_current_user)):
    return await role_section_controller.get_all_role_sections()

@role_section_router.get("/get_by_id/{role_section_id}")
async def get_role_section_by_id(role_section_id: int, _: dict = Depends(get_current_user)):
    return await role_section_controller.get_role_section_by_id(role_section_id)

@role_section_router.get("/get_all_by_role_id/{role_id}")
async def get_all_role_sections_by_role_id(role_id: int, _: dict = Depends(get_current_user)):
    return await role_section_controller.get_all_role_sections_by_role_id(role_id)

@role_section_router.get("/get_all_by_section_id/{section_id}")
async def get_all_role_sections_by_section_id(section_id: int, _: dict = Depends(get_current_user)):
    return await role_section_controller.get_all_role_sections_by_section_id(section_id)

@role_section_router.post("/create")
async def create_role_section(role_section: RoleSection, _: dict = Depends(get_current_user)):
    return await role_section_controller.create_role_section(role_section)

@role_section_router.delete("/delete/{role_section_id}")
async def delete_role_section(role_section_id: int, _: dict = Depends(get_current_user)):
    return await role_section_controller.delete_role_section(role_section_id)