from sqlmodel import Field, SQLModel

class Section(SQLModel, table=True):
    section_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True)
    description: str = Field(nullable=False)
    is_active: bool = Field(default=True, nullable=False)

    __tablename__ = "sections"