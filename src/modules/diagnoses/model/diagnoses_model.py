
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
if TYPE_CHECKING:
    from src.modules.users.model.users_model import User

class Diagnoses(SQLModel, table=True):
    diagnosis_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id", nullable=False)
    pregnancies: int = Field(nullable=False)
    glucose: int = Field(nullable=False)
    blood_pressure: int = Field(nullable=False)
    skin_thickness: int = Field(nullable=False)
    insulin: int = Field(nullable=False)
    bmi: float = Field(nullable=False)
    diabetes_pedigree_function: float = Field(nullable=False)
    age: int = Field(nullable=False)
    result: int = Field(nullable=False)

    user: "User" = Relationship(back_populates="diagnoses")
    __tablename__ = "diagnoses"