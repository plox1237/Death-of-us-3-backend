from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from src.modules.roles.model.roles_model import Role
    from src.modules.sections.model.sections_model import Section

class RoleSection(SQLModel, table=True):
    role_section_id: int | None = Field(default=None, primary_key=True)
    role_id: int = Field(foreign_key="roles.role_id", nullable=False)
    section_id: int = Field(foreign_key="sections.section_id", nullable=False)

    role: "Role" = Relationship(back_populates="role_sections")
    section: "Section" = Relationship(back_populates="role_sections")
    __tablename__ = "role_sections"