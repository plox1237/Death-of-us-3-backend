from fastapi import APIRouter
from src.modules.users.model.users_model import User
from src.modules.users.controllers.users_controller import UsersController

user_router = APIRouter()
users_controller = UsersController()

@user_router.get("/get_all")
async def get_all_users():
    return await users_controller.get_all_users()

@user_router.get("/get_by_id/{user_id}")
async def get_user_by_id(user_id: int):
    return await users_controller.get_user_by_id(user_id)

@user_router.get("/get_by_email/{email}")
async def get_user_by_email(email: str):
    return await users_controller.get_user_by_email(email)

@user_router.get("/get_by_phone/{phone}")
async def get_user_by_phone(phone: str):
    return await users_controller.get_user_by_phone(phone)

@user_router.post("/create")
async def create_user(user: User):
    return await users_controller.create_user(user)

@user_router.put("/update/{user_id}")
async def update_user(user_id: int, user: User):
    return await users_controller.update_user(user_id, user)

@user_router.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    return await users_controller.delete_user(user_id)