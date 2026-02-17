from sqlmodel import Session, select
from src.modules.users.model.users_model import User

class UsersRepository: 
    def __init__(self, session: Session):
        self.session = session
    
    async def get_all_users(self):
        statement = select(User).order_by(User.user_id)
        results = self.session.exec(statement)
        return results.all()

    async def get_user_by_id(self, user_id: int):
        statement = select(User).where(User.user_id == user_id)
        result = self.session.exec(statement)
        return result.first()
    
    async def get_user_by_email(self, email: str):
        statement = select(User).where(User.email == email)
        result = self.session.exec(statement)
        return result.first()
    
    async def get_user_by_phone(self, phone: str):
        statement = select(User).where(User.phone == phone)
        result = self.session.exec(statement)
        return result.first()
    
    async def create_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return
    
    async def update_user(self, user: User):
        statement = select(User).where(User.user_id == user_id)
        user_db = self.session.exec(statement).first()
        if user.name:
            user_db.name = user.name
        if user.last_name:
            user_db.last_name = user.last_name
        if user.email:
            user_db.email = user.email
        if user.password:
            user_db.password = user.password
        if user.phone:
            user_db.phone = user.phone
        self.session.commit()
    
    async def delete_user(self, user: User):
        self.session.delete(user)
        self.session.commit()

