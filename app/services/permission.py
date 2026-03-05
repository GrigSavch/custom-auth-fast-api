from sqlalchemy import select
from fastapi import HTTPException
from app.models.role import UserRole
from app.models.access import AccessRoleRule, BusinessElement

async def check_permission(user, element_name, action, session, owner_id=None):

    roles = await session.execute(
        select(UserRole.role_id).where(UserRole.user_id == user.id)
    )
    role_ids = [r[0] for r in roles.all()]

    element = await session.execute(
        select(BusinessElement).where(BusinessElement.name == element_name)
    )
    element = element.scalar_one()

    rules = await session.execute(
        select(AccessRoleRule)
        .where(AccessRoleRule.role_id.in_(role_ids))
        .where(AccessRoleRule.element_id == element.id)
    )

    for rule in rules.scalars():
        if getattr(rule, f"{action}_all_permission"):
            return True
        if getattr(rule, f"{action}_permission") and owner_id == user.id:
            return True

    raise HTTPException(status_code=403, detail="Forbidden")