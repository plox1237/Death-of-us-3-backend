from jwt import encode, decode, exceptions, get_unverified_header
import jwt
import datetime
from dotenv import load_dotenv
import os
import requests
from fastapi import HTTPException
from src.modules.users.model.users_model import User

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

AZURE_TENANT_ID = os.getenv("AZURE_TENANT_ID")
AZURE_CLIENT_ID = os.getenv("AZURE_CLIENT_ID")

OPENID_CONFIG_URL = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/v2.0/.well-known/openid-configuration"

config = requests.get(OPENID_CONFIG_URL).json()
JWKS_URI = config["jwks_uri"]
jwks = requests.get(JWKS_URI).json()

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

def validate_local_token(token: str):
    payload = decode(
        token,
        key=SECRET_KEY,
        algorithms=["HS256"]
    )
    payload["auth_provider"] = "local"
    return payload

def validate_azure_token(token: str):
    try:
        unverified_header = get_unverified_header(token)
        rsa_key = None
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key is None:
            raise HTTPException(status_code=401, detail="AZURE KEY NOT FOUND")
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=["RS256"],
            audience=AZURE_CLIENT_ID,
            issuer=f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/v2.0"
        )
        payload["auth_provider"] = "azure"
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="INVALID AZURE TOKEN")


async def validate_token(token: str):
    try:
        return validate_local_token(token)
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="EXPIRED TOKEN")
    except exceptions.PyJWTError:
        pass

    try:
        return validate_azure_token(token)
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="EXPIRED AZURE TOKEN")
    except exceptions.PyJWTError:
        raise HTTPException(status_code=401, detail="INVALID TOKEN")