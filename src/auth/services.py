import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import AccessToken
from core.db import get_async_session
from settings import ALGORITHM, JWT_SECRET
from users.models import User as UserModel
from users.schemas import User
from users.services import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")


async def authenticate_user(email: str, password: str, db: AsyncSession) -> UserModel:
    user = await get_user_by_email(email, db)
    if not user or not user.verify_password(password):
        return None
    return user


async def create_token(user: UserModel, db: AsyncSession) -> AccessToken:
    user = User.model_validate(user)
    token = jwt.encode(user.dict(), JWT_SECRET, algorithm=ALGORITHM)
    return {'access_token': token, 'token_type': "bearer"}


async def get_current_user(db: AsyncSession = Depends(get_async_session), token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        user = await get_user_by_email(payload.get("email"), db)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:  # noqa
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    return User.model_validate(user)
