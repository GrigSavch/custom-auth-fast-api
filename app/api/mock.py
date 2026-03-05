from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user
from app.services.permission import check_permission
from database import get_session

router = APIRouter()

@router.get("/products")
async def get_products(
    user=Depends(get_current_user),
    session=Depends(get_session)
):
    await check_permission(user, "products", "read", session)
    return ["Product 1", "Product 2"]