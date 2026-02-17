from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.modules.users.services.users_service import UsersService
from src.modules.users.model.users_model import User

class UsersController:
    def __init__(self):
        self.service = UsersService()
    
    async def get_all_users(self):
        try:
            users = await self.service.get_all_users()
            data = jsonable_encoder(users)
            return JSONResponse(status_code=200, content={
                "message": "USERS FOUND",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING ALL USERS: \n", e)
            raise e
    
    async def get_user_by_id(self, user_id: int):
        try:
            user = await self.service.get_user_by_id(user_id)
            data = jsonable_encoder(user)
            return JSONResponse(status_code=200, content={
                "message": "USER FOUND",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING USER BY ID: \n", e)
            raise e
    
    async def get_user_by_email(self, email: str):
        try:
            user = await self.service.get_user_by_email(email)
            data = jsonable_encoder(user)
            return JSONResponse(status_code=200, content={
                "message": "USER FOUND",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING USER BY EMAIL: \n", e)
            raise e

    async def get_user_by_phone(self, phone: str):
        try:
            user = await self.service.get_user_by_phone(phone)
            data = jsonable_encoder(user)
            return JSONResponse(status_code=200, content={
                "message": "USER FOUND",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING USER BY PHONE: \n", e)
            raise e
    
    async def create_user(self, user: User):
        try:
            await self.service.create_user(user)
            return JSONResponse(status_code=201, content={
                "message": "USER CREATED",
            })
        except Exception as e:
            print("ERROR DURING CREATING USER: \n", e)
            raise e
    
    async def update_user(self, user_id: int, user: User):
        try:
            await self.service.update_user(user_id, user)
            return JSONResponse(status_code=200, content={
                "message": "USER UPDATED"
            })
        except Exception as e:
            print("ERROR DURING UPDATING USER: \n", e)
            raise e
    
    async def delete_user(self, user_id: int):
        try:
            await self.service.delete_user(user_id)
            return JSONResponse(status_code=200, content={
                "message": "USER DELETED"
            })
        except Exception as e:
            print("ERROR DURING DELETING USER: \n", e)
            raise e