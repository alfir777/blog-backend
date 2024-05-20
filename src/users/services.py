import passlib.hash as _hash
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from users.models import User as UserModel
from users.schemas import UserCreate

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")


async def get_user_by_email(email: str, db: AsyncSession) -> UserModel:
    result = await db.execute(select(UserModel).where(UserModel.email == email))
    return result.scalars().first()


async def get_user_by_username(username: str, db: AsyncSession) -> UserModel:
    result = await db.execute(select(UserModel).where(UserModel.username == username))
    return result.scalars().first()


async def create_user_db(user: UserCreate, db: AsyncSession) -> UserModel:
    db_user = UserModel(username=user.username, email=user.email, hashed_password=_hash.bcrypt.hash(user.password))
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
