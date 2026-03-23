from sqlmodel import Session, select
from src.modules.users.model.users_model import User

class UsersRepository: 
    def __init__(self, session: Session):
        self.session = session
    
    async def get_all_users(self):
        try:
            statement = select(User).order_by(User.user_id)
            results = self.session.exec(statement).all()
            return [
            {
                "user_id": u.user_id,
                "name": u.name,
                "last_name": u.last_name,
                "email": u.email,
                "phone": u.phone,
                "role": {
                    "role_id": u.role.role_id,
                    "name": u.role.name
                }
            }
            for u in results
        ]
        except Exception as e:
            self.session.rollback()
            raise e

    async def get_user_by_id(self, user_id: int):
        try:
            statement = select(User).where(User.user_id == user_id)
            result = self.session.exec(statement).first()
            return {
                "user_id": result.user_id,
                "name": result.name,
                "last_name": result.last_name,
                "email": result.email,
                "phone": result.phone,
                "role": {
                    "role_id": result.role.role_id,
                    "name": result.role.name
                }
            }
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def get_user_by_email(self, email: str):
        try:
            statement = select(User).where(User.email == email)
            result = self.session.exec(statement).first()
            return {
                "user_id": result.user_id,
                "name": result.name,
                "last_name": result.last_name,
                "email": result.email,
                "phone": result.phone,
                "role": {
                    "role_id": result.role.role_id,
                    "name": result.role.name
                }
            }
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def get_user_by_phone(self, phone: str):
        try:
            statement = select(User).where(User.phone == phone)
            result = self.session.exec(statement).first()
            return {
                "user_id": result.user_id,
                "name": result.name,
                "last_name": result.last_name,
                "email": result.email,
                "phone": result.phone,
                "role": {
                    "role_id": result.role.role_id,
                    "name": result.role.name
                }
            }
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def create_user(self, user: User):
        try:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def update_user(self,user_id: int, user: User):
        try:
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
        except Exception as e:
            self.session.rollback()
            raise e

    async def delete_user(self, user: User):
        try:
            self.session.delete(user)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

