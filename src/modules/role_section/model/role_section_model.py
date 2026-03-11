from sqlmodel import SQLModel, Field

class RoleSection(SQLModel, table=True):
    role_section_id: int | None = Field(default=None, primary_key=True)
    role_id: int
    section_id: int