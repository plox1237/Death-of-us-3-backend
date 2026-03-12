from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.shared.utils.jwt_utils import validate_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = await validate_token(token)
    if payload.get("auth_provider") == "azure":
        email = payload.get("preferred_username")
        user = await user_repository.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=403, detail="USER NOT REGISTERED")
        payload["user_role"] = user.role_id
        payload["user_id"] = user.user_id
    return payload
