from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.modules.auth.schema.auth_schema import AuthSchema
from src.modules.auth.controllers.auth_controller import login_user


auth_router = APIRouter()

@auth_router.post("/login")
async def login_user_route(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_user(form_data)
