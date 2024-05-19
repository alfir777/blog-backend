from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from auth.services import authenticate_user, create_token
from core.db import get_async_session

router_auth_v1 = APIRouter(tags=['auth'])


@router_auth_v1.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(),
                         db: AsyncSession = Depends(get_async_session)):
    user = await authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    return await create_token(user, db)
