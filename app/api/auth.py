from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from database import SessionDep
from app.models.user import User, UserCreateSchema
from app.auth.security import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register")
async def register(data: UserCreateSchema, session: SessionDep):
    user = User(
        email=data.email,
        password_hash=hash_password(data.password),
        first_name=data.first_name,
        last_name=data.last_name,
        middle_name=data.middle_name
    )
    session.add(user)
    await session.commit()
    return {"msg": "registered"}

@router.post("/login")
async def login(data, session: SessionDep):
    result = await session.execute(select(User).where(User.email == data["email"]))
    user = result.scalar_one_or_none()

    if not user or not verify_password(data["password"], user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": create_access_token(user.id)}