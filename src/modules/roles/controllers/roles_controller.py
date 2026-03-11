from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.modules.roles.model.roles_model import Role
from src.modules.roles.services.roles_service import RolesService

class RolesController:
    def __init__(self):
        self.service = RolesService()

    async def get_all_roles(self):
        try:
            roles = await self.service.get_all_roles()
            data = jsonable_encoder(roles)
            return JSONResponse(status_code=200, content={
                "message": "ROLES FOUND",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING ALL ROLES: \n", e)
            raise e
        
    async def get_role_by_id(self, role_id: int):
        try:
            role = await self.service.get_role_by_id(role_id)
            data = jsonable_encoder(role)
            return JSONResponse(status_code=200, content={
                "message": "ROLE FOUND",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING ROLE BY ID: \n", e)
            raise e
    
    async def get_role_by_name(self, name: str):
        try:
            role = await self.service.get_role_by_name(name)
            data = jsonable_encoder(role)
            return JSONResponse(status_code=200, content={
                "message": "ROLE FOUND",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING ROLE BY NAME: \n", e)
            raise e
    
    async def create_role(self, role: Role):
        try:
            await self.service.create_role(role)
            return JSONResponse(status_code=201, content={
                "message": "ROLE CREATED",
            })
        except Exception as e:
            print("ERROR DURING CREATING ROLE: \n", e)
            raise e
    
    async def update_role(self, role_id: int, role: Role):
        try:
            await self.service.update_role(role_id, role)
            return JSONResponse(status_code=200, content={
                "message": "ROLE UPDATED",
            })
        except Exception as e:
            print("ERROR DURING UPDATING ROLE: \n", e)
            raise e
    
    async def delete_role(self, role_id: int):
        try:
            await self.service.delete_role(role_id)
            return JSONResponse(status_code=200, content={
                "message": "ROLE DELETED",
            })
        except Exception as e:
            print("ERROR DURING DELETING ROLE: \n", e)
            raise e
