from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from app.models.base import Base

from pydantic import BaseModel, Field, EmailStr, ConfigDict

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[str | None]
    password_hash: Mapped[str]
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    roles = relationship("UserRole", back_populates="user")

# МОЁ
class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str = Field(max_length=30)
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)
    middle_name: str | None = Field(max_length=30)

    model_config = ConfigDict(extra='forbid')