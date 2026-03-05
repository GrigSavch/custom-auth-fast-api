from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, ForeignKey
from app.models.base import Base

class BusinessElement(Base):
    __tablename__ = "business_elements"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

class AccessRoleRule(Base):
    __tablename__ = "access_role_rules"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    element_id: Mapped[int] = mapped_column(ForeignKey("business_elements.id"))

    read_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    read_all_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    create_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    update_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    update_all_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    delete_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    delete_all_permission: Mapped[bool] = mapped_column(Boolean, default=False)