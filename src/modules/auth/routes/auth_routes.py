from fastapi import APIRouter
from src.modules.auth.schema.auth_schema import AuthSchema
from src.modules.auth.controllers.auth_controller import login_user

auth_router = APIRouter()

@auth_router.post("/login")
async def login_user_route(user: AuthSchema):
    return await login_user(user)