from fastapi import HTTPException
from sqlmodel import Session
from modules.roles.repositories import roles_repository
from src.config.database import engine
from src.modules.roles.model.roles_model import Role
from src.modules.roles.repositories.roles_repository import RolesRepository

roles_repository = RolesRepository(Session(engine))

class RolesService:
    def __init__(self):
        self.repository = roles_repository

    async def get_all_roles(self):
        roles = await self.repository.get_all_roles()
        if not roles:
            raise HTTPException(status_code=404, detail="ROLES NOT FOUND")
        return roles
    
    async def get_role_by_id(self, role_id: int):
        role = await self.repository.get_role_by_id(role_id)
        if not role:
            raise HTTPException(status_code=404, detail="ROLE NOT FOUND")
        return role
    
    async def get_role_by_name(self, name: str):
        role = await self.repository.get_role_by_name(name)
        if not role:
            raise HTTPException(status_code=404, detail="ROLE NOT FOUND")
        return role
    
    async def create_role(self, role: Role):
        role_db = await self.repository.get_role_by_name(role.name)
        if role_db:
            raise HTTPException(status_code=409, detail="ROLE ALREADY EXISTS")
        await self.repository.create_role(role)
        return
    
    async def update_role(self, role_id: int, role: Role):
        role_db = await self.repository.get_role_by_id(role_id)
        if not role_db:
            raise HTTPException(status_code=404, detail="ROLE NOT FOUND")
        role_db.name = role.name
        self.repository.update_role(role_db)
        return role_db
    
    async def delete_role(self, role_id: int):
        role_db = await self.repository.get_role_by_id(role_id)
        if not role_db:
            raise HTTPException(status_code=404, detail="ROLE NOT FOUND")
        await self.repository.delete_role(role_db)
        return