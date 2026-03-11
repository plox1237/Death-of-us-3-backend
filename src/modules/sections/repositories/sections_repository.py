from sqlmodel import func, select, Session
from src.modules.sections.model.sections_model import Section

class SectionsRepository:
    def __init__(self, session: Session):
        self.session = session
    
    async def get_all_sections(self):
        statement = select(Section).order_by(Section.section_id)
        results = self.session.exec(statement)
        return results.all()
    
    async def get_section_by_id(self, section_id: int):
        statement = select(Section).where(Section.section_id == section_id)
        result = self.session.exec(statement)
        return result.first()
    
    async def get_section_by_name(self, name: str):
        statement = select(Section).where(
            func.lower(Section.name) == func.lower(name)
        )
        result = self.session.exec(statement)
        return result.first()
    
    async def create_section(self, section: Section):
        try:
            self.session.add(section)
            self.session.commit()
            self.session.refresh(section)
            return section
        except Exception as e:
            self.session.rollback()
            raise e
    
    async def update_section(self, section: Section, section_id: int):
        try:
            statement = select(Section).where(Section.section_id == section_id)
            section_db = self.session.exec(statement).first()
            if section.name:
                section_db.name = section.name
            if section.description:
                section_db.description = section.description
            if section.is_active:
                section_db.is_active = section.is_active
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    async def delete_section(self, section: Section):
        self.session.delete(section)
        self.session.commit()
        