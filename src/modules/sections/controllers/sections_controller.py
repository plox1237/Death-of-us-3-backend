from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.modules.sections.services.sections_service import SectionsService
from src.modules.sections.model.sections_model import Section

class SectionsController:
    def __init__(self):
        self.service = SectionsService()
    
    async def get_all_sections(self):
        try:
            sections = await self.service.get_all_sections()
            data = jsonable_encoder(sections)
            return JSONResponse(content={
                "message": "SECTIONS FOUND",
                "data": data
            }, status_code=200)
        except Exception as e:
            print("ERROR DURING GETTING ALL SECTIONS: \n", e)
            raise e
    
    async def get_section_by_id(self, section_id: int):
        try:
            section = await self.service.get_section_by_id(section_id)
            data = jsonable_encoder(section)
            return JSONResponse(content={
                "message": "SECTION FOUND",
                "data": data
            }, status_code=200)
        except Exception as e:
            print("ERROR DURING GETTING SECTION BY ID: \n", e)
            raise e
        
    async def get_section_by_name(self, name: str):
        try:
            section = await self.service.get_section_by_name(name)
            data = jsonable_encoder(section)
            return JSONResponse(content={
                "message": "SECTION FOUND",
                "data": data
            }, status_code=200)
        except Exception as e:
            print("ERROR DURING GETTING SECTION BY NAME: \n", e)
            raise e
        
    async def create_section(self, section: Section):
        try:
            await self.service.create_section(section)
            return JSONResponse(content={
                "message": "SECTION CREATED",
                "data": jsonable_encoder(section)
            }, status_code=201)
        except Exception as e:
            print("ERROR DURING CREATING SECTION: \n", e)
            raise e
    
    async def update_section(self, section_id: int, section: Section):
        try:
            await self.service.update_section(section=section, section_id=section_id)
            return JSONResponse(content={
                "message": "SECTION UPDATED",
            }, status_code=200)
        except Exception as e:
            print("ERROR DURING UPDATING SECTION: \n", e)
            raise e
    
    async def delete_section(self, section_id: int):
        try:
            await self.service.delete_section(section_id=section_id)
            return JSONResponse(content={
                "message": "SECTION DELETED",
            }, status_code=200)
        except Exception as e:
            print("ERROR DURING DELETING SECTION: \n", e)
            raise e