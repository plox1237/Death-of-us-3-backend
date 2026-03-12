from fastapi import HTTPException, Depends
from sqlmodel import Session
from src.config.database import engine
from src.modules.role_section.repositories.role_section_repository import RoleSectionRepository
from src.modules.auth.dependencies.auth_dependencies import get_current_user

role_section_repository = RoleSectionRepository(Session(engine))

def require_section(section_id: int):
    def wrapper(current_user: dict = Depends(get_current_user)):
        access = role_section_repository.get_role_section_by_role_id_and_section_id(
            role_id=current_user["user_role"],
            section_id=section_id
        )
        if not access:
            raise HTTPException(status_code=403, detail="ACCESS DENIED: YOU DON'T HAVE PERMISSION FOR THIS SECTION")
        return current_user
    return wrapper