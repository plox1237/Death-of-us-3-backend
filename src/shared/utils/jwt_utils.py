from jwt import encode, decode, exceptions
import datetime
from dotenv import load_dotenv
import os
from fastapi import HTTPException
from src.modules.users.model.users_model import User

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

async def generate_token(user: User):
    payload = {
        "user_id": user.user_id,
        "user_role": user.role_id,
        "user_email": user.email,
        "user_phone": user.phone,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = encode(payload=payload, key=SECRET_KEY, algorithm="HS256")
    return token

async def validate_token(token: str):
    try:
        payload = decode(token, key=SECRET_KEY, algorithms=["HS256"])
        return payload
    except exceptions.DecodeError:
        raise HTTPException(status_code=401, detail="INVALID TOKEN")
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="EXPIRED TOKEN")