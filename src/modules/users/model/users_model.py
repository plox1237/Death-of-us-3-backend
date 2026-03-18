from typing import TYPE_CHECKING, List
from sqlmodel import Field, SQLModel, Relationship
if TYPE_CHECKING:
    from src.modules.roles.model.roles_model import Role
    from src.modules.diagnoses.model.diagnoses_model import Diagnoses
class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    password: str = Field(nullable=False)
    phone: str = Field(index=True, unique=True, nullable=False)
    role_id: int = Field(foreign_key="roles.role_id", nullable=False)

    role: "Role" = Relationship(back_populates="users")
    diagnoses: List["Diagnoses"] = Relationship(back_populates="user")
    __tablename__ = "users"