from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy import select
import jwt

from database import get_session
from app.models.user import User
from config import settings

security = HTTPBearer()

async def get_current_user(credentials=Depends(security), session=Depends(get_session)):
    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        user_id = payload["sub"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="User inactive")

    return user