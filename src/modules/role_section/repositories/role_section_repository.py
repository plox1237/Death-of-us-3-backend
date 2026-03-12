from sqlmodel import select, Session
from src.modules.role_section.model.role_section_model import RoleSection

class RoleSectionRepository:
    def __init__(self, session: Session):
        self.session = session
    
    async def get_all_role_sections(self):
        try:
            statement = select(RoleSection).order_by(RoleSection.role_section_id)
            results = self.session.exec(statement).all()
            return results
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def get_role_section_by_id(self, role_section_id: int):
        try:
            statement = select(RoleSection).where(RoleSection.role_section_id == role_section_id)
            result = self.session.exec(statement).first()
            return result
        except Exception as e:
            self.session.rollback()
            raise e

    async def get_all_role_sections_by_role_id(self, role_id: int):
        try:
            statement = select(RoleSection).where(RoleSection.role_id == role_id).order_by(RoleSection.role_section_id)
            results = self.session.exec(statement).all()
            return results
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def get_all_role_sections_by_section_id(self, section_id: int):
        try:
            statement = select(RoleSection).where(RoleSection.section_id == section_id).order_by(RoleSection.role_section_id)
            results = self.session.exec(statement).all()
            return results
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def get_role_section_by_role_id_and_section_id(self, role_id: int, section_id: int):
        try:
            statement = select(RoleSection).where(RoleSection.role_id == role_id, RoleSection.section_id == section_id)
            result = self.session.exec(statement).first()
            return result
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def create_role_section(self, role_section: RoleSection):
        try:
            self.session.add(role_section)
            self.session.commit()
            self.session.refresh(role_section)
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def delete_role_section(self, role_section: RoleSection):
        try:
            self.session.delete(role_section)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e