from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.modules.auth.schema.auth_schema import AuthSchema
from src.modules.auth.services.auth_service import login_user_service

async def login_user(user: AuthSchema):
    try:
        user = await login_user_service(user.email, user.password)
        user_dict = jsonable_encoder(user)
        user_dict.pop("password")
        print(user_dict)
        return JSONResponse(content={
            "message": "LOGIN SUCCESSFUL",
            "user": user_dict
        }, status_code=200)
    except Exception as e:
        print("ERROR DURING LOGIN: \n", e)
        raise e