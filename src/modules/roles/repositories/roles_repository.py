from sqlmodel import Session, select
from src.modules.roles.model.roles_model import Role

class RolesRepository:
    def __init__(self, session: Session):
        self.session = session

    async def get_all_roles(self):
        statement = select(Role).order_by(Role.role_id)
        roles = self.session.exec(statement).all()
        return roles
    
    async def get_role_by_id(self, role_id: int):
        statement = select(Role).where(Role.role_id == role_id)
        role = self.session.exec(statement).first()
        return role
    
    async def get_role_by_name(self, name: str):
        statement = select(Role).where(Role.name == name)
        role = self.session.exec(statement).first()
        return role
    
    async def create_role(self, role: Role):
        self.session.add(role)
        self.session.commit()
        self.session.refresh(role)
        return
    
    async def update_role(self, role: Role, role_id: int):
        statement = select(Role).where(Role.role_id == role_id)
        role_db = self.session.exec(statement).first()
        if role.name:
            role_db.name = role.name
        self.session.commit()
    
    async def delete_role(self, role: Role):
        self.session.delete(role)
        self.session.commit()
    
