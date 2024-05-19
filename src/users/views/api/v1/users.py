from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import AccessToken
from auth.services import create_token, get_current_user
from core.db import get_async_session
from users.schemas import User, UserCreate
from users.services import create_user_db, get_user_by_email, get_user_by_username

router_users_v1 = APIRouter(tags=['users'])


@router_users_v1.post('', response_model=AccessToken)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_async_session)) -> AccessToken:
    db_user_by_email = await get_user_by_email(user.email, db)
    db_user_by_username = await get_user_by_username(user.username, db)
    if db_user_by_email:
        return HTTPException(status_code=400, detail="Email already registered")
    if db_user_by_username:
        return HTTPException(status_code=400, detail="Username already registered")
    user = await create_user_db(user, db)
    return await create_token(user, db)


@router_users_v1.get('/me', response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)) -> User:
    return current_user
