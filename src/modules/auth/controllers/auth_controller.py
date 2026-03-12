from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from src.modules.auth.schema.auth_schema import AuthSchema
from src.modules.auth.services.auth_service import login_user_service

async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        data = await login_user_service(form_data.username, form_data.password)
        user_dict = jsonable_encoder(data)
        return JSONResponse(content={
            "message": "LOGIN SUCCESSFUL",
            "token_type": "Bearer",
            "access_token": user_dict["access_token"],
            "user_id": user_dict["user_id"],
            "user_email": user_dict["user_email"],
            "user_phone": user_dict["user_phone"],
            "user_role": user_dict["user_role"]   
        }, status_code=200)
    except Exception as e:
        print("ERROR DURING LOGIN: \n", e)
        raise e