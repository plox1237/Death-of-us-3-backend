from fastapi import HTTPException
from src.modules.users.services.users_service import user_repository

async def login_user_service(email: str, password: str):
    user = await user_repository.get_user_by_email(email)
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="INVALID CREDENTIALS")
    return user 