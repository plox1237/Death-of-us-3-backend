from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    password: str = Field(nullable=False)
    phone: str = Field(index=True, unique=True, nullable=False)

    __tablename__ = "users"