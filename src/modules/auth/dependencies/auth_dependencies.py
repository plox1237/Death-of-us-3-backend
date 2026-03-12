from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.shared.utils.jwt_utils import validate_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = await validate_token(token)
    return payload
