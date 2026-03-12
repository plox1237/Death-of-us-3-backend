from sqlmodel import Session, func, select
from src.modules.roles.model.roles_model import Role

class RolesRepository:
    def __init__(self, session: Session):
        self.session = session

    async def get_all_roles(self):
        try:
            statement = select(Role).order_by(Role.role_id)
            roles = self.session.exec(statement).all()
            return roles
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def get_role_by_id(self, role_id: int):
        try:
            statement = select(Role).where(Role.role_id == role_id)
            role = self.session.exec(statement).first()
            return role
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def get_role_by_name(self, name: str):
        try:
            statement = select(Role).where(
                func.lower(Role.name) == func.lower(name)
            )
            role = self.session.exec(statement).first()
            return role
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def create_role(self, role: Role):
        try:
            self.session.add(role)
            self.session.commit()
            self.session.refresh(role)
            return
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def update_role(self, role: Role, role_id: int):
        try:
            statement = select(Role).where(Role.role_id == role_id)
            role_db = self.session.exec(statement).first()
            if role.name:
                role_db.name = role.name
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def delete_role(self, role: Role):
        try:
            self.session.delete(role)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
    
