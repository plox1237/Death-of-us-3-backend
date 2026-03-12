from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.modules.role_section.model.role_section_model import RoleSection
from src.modules.role_section.services.role_section_service import RoleSectionService

role_section_service = RoleSectionService()

class RoleSectionController:
    def __init__(self):
        self.service = role_section_service
    
    async def get_all_role_sections(self):
        try:
            role_sections = await self.service.get_all_role_sections()
            data = jsonable_encoder(role_sections)
            return JSONResponse(status_code=200, content={
                "message": "ROLE SECTIONS FOUND",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING ALL ROLE SECTIONS: \n", e)
            raise e
    
    async def get_role_section_by_id(self, role_section_id: int):
        try:
            role_section = await self.service.get_role_section_by_id(role_section_id)
            data = jsonable_encoder(role_section)
            return JSONResponse(status_code=200, content={
                "message": "ROLE SECTION FOUND",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING ROLE SECTION BY ID: \n", e)
            raise e
    
    async def get_all_role_sections_by_role_id(self, role_id: int):
        try:
            role_sections = await self.service.get_all_role_sections_by_role_id(role_id)
            data = jsonable_encoder(role_sections)
            return JSONResponse(status_code=200, content={
                "message": "ROLE SECTIONS FOUND FOR THIS ROLE",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING ALL ROLE SECTIONS BY ROLE ID: \n", e)
            raise e
    
    async def get_all_role_sections_by_section_id(self, section_id: int):
        try:
            role_sections = await self.service.get_all_role_sections_by_section_id(section_id)
            data = jsonable_encoder(role_sections)
            return JSONResponse(status_code=200, content={
                "message": "ROLE SECTIONS FOUND FOR THIS SECTION",
                "data": data
            })
        except Exception as e:
            print("ERROR DURING GETTING ALL ROLE SECTIONS BY SECTION ID: \n", e)
            raise e
    
    async def create_role_section(self, role_section: RoleSection):
        try:
            await self.service.create_role_section(role_section)
            return JSONResponse(status_code=201, content={
                "message": "ROLE SECTION CREATED",
            })
        except Exception as e:
            print("ERROR DURING CREATING ROLE SECTION: \n", e)
            raise e
    
    async def delete_role_section(self, role_section_id: int):
        try:
            await self.service.delete_role_section(role_section_id)
            return JSONResponse(status_code=200, content={
                "message": "ROLE SECTION DELETED",
            })
        except Exception as e:
            print("ERROR DURING DELETING ROLE SECTION: \n", e)
            raise e