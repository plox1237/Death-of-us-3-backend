from fastapi import APIRouter
from src.modules.users.routes.users_routes import user_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])