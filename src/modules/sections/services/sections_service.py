from fastapi import HTTPException
from sqlmodel import Session
from src.config.database import engine
from src.modules.sections.model.sections_model import Section
from src.modules.sections.repositories.sections_repository import SectionsRepository

sections_repository = SectionsRepository(Session(engine))

class SectionsService:
    def __init__(self):
        self.repository = sections_repository
    
    async def get_all_sections(self):
        sections = await self.repository.get_all_sections()
        if not sections:
            raise HTTPException(status_code=404, detail="SECTIONS NOT FOUND")
        return sections

    async def get_section_by_id(self, section_id: int):
        section = await self.repository.get_section_by_id(section_id)
        if not section:
            raise HTTPException(status_code=404, detail="SECTION NOT FOUND")
        return section
    
    async def get_section_by_name(self, name: str):
        section = await self.repository.get_section_by_name(name)
        if not section:
            raise HTTPException(status_code=404, detail="SECTION NOT FOUND")
        return section
    
    async def create_section(self, section: Section):
        section_db = await self.repository.get_section_by_name(section.name)
        if section_db:
            raise HTTPException(status_code=409, detail="SECTION ALREADY EXISTS")
        await self.repository.create_section(section)
        return
    
    async def update_section(self, section: Section, section_id: int):
        section_db = await self.repository.get_section_by_id(section_id)
        if not section_db:
            raise HTTPException(status_code=404, detail="SECTION NOT FOUND")
        possible_section = await self.repository.get_section_by_name(section.name)
        if possible_section and possible_section.section_id != section_id:
            raise HTTPException(status_code=409, detail="SECTION NAME ALREADY EXISTS")   
        await self.repository.update_section(section, section_id)
        return
    
    async def delete_section(self, section_id: int):
        section_db = await self.repository.get_section_by_id(section_id)
        if not section_db:
            raise HTTPException(status_code=404, detail="SECTION NOT FOUND")
        await self.repository.delete_section(section_db)
        return