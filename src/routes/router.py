from fastapi import APIRouter
from src.modules.users.routes.users_routes import user_router
from src.modules.auth.routes.auth_routes import auth_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(auth_router, prefix="/auth", tags=["Auth"])