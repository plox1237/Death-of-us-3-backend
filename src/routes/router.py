from fastapi import APIRouter
from src.modules.role_section.routes.role_section_routes import role_section_router
from src.modules.users.routes.users_routes import user_router
from src.modules.auth.routes.auth_routes import auth_router
from src.modules.sections.routes.sections_routes import sections_router
from src.modules.roles.routes.roles_routes import roles_router
from src.modules.prediction.routes.predict_routes import predict_router
from src.modules.diagnoses.routes.diagnoses_routes import diagnoses_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(sections_router, prefix="/sections", tags=["Sections"])
router.include_router(roles_router, prefix="/roles", tags=["Roles"])
router.include_router(role_section_router, prefix="/role_sections", tags=["Role Sections"])
router.include_router(predict_router, prefix="/predict", tags=["Prediction"])
router.include_router(diagnoses_router, prefix="/diagnoses", tags=["Diagnoses"])