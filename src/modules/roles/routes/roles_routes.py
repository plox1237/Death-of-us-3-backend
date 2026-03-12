from fastapi import APIRouter, Depends
from src.modules.auth.dependencies.auth_dependencies import get_current_user
from src.modules.roles.model.roles_model import Role
from src.modules.roles.controllers.roles_controller import RolesController

roles_router = APIRouter()
roles_controller = RolesController()

@roles_router.get("/get_all")
async def get_all_roles(_: dict = Depends(get_current_user)):
    return await roles_controller.get_all_roles()

@roles_router.get("/get_by_id/{role_id}")
async def get_role_by_id(role_id: int, _: dict = Depends(get_current_user)):
    return await roles_controller.get_role_by_id(role_id)

@roles_router.get("/get_by_name/{name}")
async def get_role_by_name(name: str, _: dict = Depends(get_current_user)):
    return await roles_controller.get_role_by_name(name)

@roles_router.post("/create")
async def create_role(role: Role, _: dict = Depends(get_current_user)):
    return await roles_controller.create_role(role)

@roles_router.put("/update/{role_id}")
async def update_role(role_id: int, role: Role, _: dict = Depends(get_current_user)):
    return await roles_controller.update_role(role_id, role)

@roles_router.delete("/delete/{role_id}")
async def delete_role(role_id: int, _: dict = Depends(get_current_user)):
    return await roles_controller.delete_role(role_id)
