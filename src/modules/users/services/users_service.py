from fastapi import HTTPException
from sqlmodel import Session
from src.config.database import engine
from src.modules.users.repositories.users_repository import UsersRepository
from src.modules.users.model.users_model import User

user_repository = UsersRepository(Session(engine))

class UsersService:
    def __init__(self):
        self.repository = user_repository
    
    async def get_all_users(self):
        users = await self.repository.get_all_users()
        if not users:
            raise HTTPException(status_code=404, detail="USERS NOT FOUND")
        return users
    
    async def get_user_by_id(self, user_id: int):
        user = await self.repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="USER NOT FOUND")
        return user
    
    async def get_user_by_email(self, email: str):
        user = await self.repository.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="USER NOT FOUND")
        return user
    
    async def get_user_by_phone(self, phone: str):
        user = await self.repository.get_user_by_phone(phone)
        if not user:
            raise HTTPException(status_code=404, detail="USER NOT FOUND")
        return user

    async def create_user(self, user: User):
        possible_user = await self.repository.get_user_by_email(user.email)
        if possible_user:
            raise HTTPException(status_code=409, detail="EMAIL ALREADY REGISTERED")
        possible_user = await self.repository.get_user_by_phone(user.phone)
        if possible_user:
            raise HTTPException(status_code=409, detail="PHONE ALREADY REGISTERED")
        await self.repository.create_user(user)
        return
    
    async def update_user(self, user_id: int, user: User):
        user_db = await self.repository.get_user_by_id(user_id)
        if not user_db: 
            raise HTTPException(status_code=404, detail="USER NOT FOUND")
        possible_user = await self.repository.get_user_by_email(user.email)
        if possible_user and possible_user.user_id != user_id:
            raise HTTPException(status_code=409, detail="EMAIL ALREADY REGISTERED")
        possible_user = await self.repository.get_user_by_phone(user.phone)
        if possible_user and possible_user.user_id != user_id:
            raise HTTPException(status_code=409, detail="PHONE ALREADY REGISTERED")
        await self.repository.update_user(user_id, user)
        return 
    
    async def delete_user(self, user_id: int):
        user_db = await self.repository.get_user_by_id(user_id)
        if not user_db:
            raise HTTPException(status_code=404, detail="USER NOT FOUND")
        await self.repository.delete_user(user_db)
        return 