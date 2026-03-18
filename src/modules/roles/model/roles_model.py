from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from src.modules.users.model.users_model import User
    from src.modules.role_section.model.role_section_model import RoleSection

class Role(SQLModel, table=True):
    role_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False, index=True)

    users: List["User"] = Relationship(back_populates="role")
    role_sections: List["RoleSection"] = Relationship(back_populates="role")
    __tablename__ = "roles"