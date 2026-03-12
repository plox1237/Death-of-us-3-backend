from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from src.modules.role_section.model.role_section_model import RoleSection

class Section(SQLModel, table=True):
    section_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True)
    description: str = Field(nullable=False)
    is_active: bool = Field(default=True, nullable=False)

    role_sections: List["RoleSection"] = Relationship(back_populates="section")
    __tablename__ = "sections"