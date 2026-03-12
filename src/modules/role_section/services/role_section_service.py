from fastapi import HTTPException
from sqlmodel import Session
from src.config.database import engine
from src.modules.role_section.model.role_section_model import RoleSection
from src.modules.role_section.repositories.role_section_repository import RoleSectionRepository

role_section_repository = RoleSectionRepository(Session(engine))

class RoleSectionService:
    def __init__(self):
        self.repository = role_section_repository
    
    async def get_all_role_sections(self):
        role_sections = await self.repository.get_all_role_sections()
        if not role_sections:
            raise HTTPException(status_code=404, detail="ROLE SECTIONS NOT FOUND")
        return role_sections
    
    async def get_role_section_by_id(self, role_section_id: int):
        role_section = await self.repository.get_role_section_by_id(role_section_id)
        if not role_section:
            raise HTTPException(status_code=404, detail="ROLE SECTION NOT FOUND")
        return role_section
    
    async def get_all_role_sections_by_role_id(self, role_id: int):
        role_sections = await self.repository.get_all_role_sections_by_role_id(role_id)
        if not role_sections:
            raise HTTPException(status_code=404, detail="ROLE SECTIONS NOT FOUND FOR THIS ROLE")
        return role_sections
    
    async def get_all_role_sections_by_section_id(self, section_id: int):
        role_sections = await self.repository.get_all_role_sections_by_section_id(section_id)
        if not role_sections:
            raise HTTPException(status_code=404, detail="ROLE SECTIONS NOT FOUND FOR THIS SECTION")
        return role_sections
    
    async def create_role_section(self, role_section: RoleSection):
        possible_role_section = await self.repository.get_role_section_by_role_id_and_section_id(role_section.role_id, role_section.section_id)
        if possible_role_section:
            raise HTTPException(status_code=409, detail="ROLE SECTION ALREADY EXISTS")
        await self.repository.create_role_section(role_section)
        return
    
    async def delete_role_section(self, role_section_id: int):
        role_section = await self.repository.get_role_section_by_id(role_section_id)
        if not role_section:
            raise HTTPException(status_code=404, detail="ROLE SECTION NOT FOUND")
        await self.repository.delete_role_section(role_section)
        return