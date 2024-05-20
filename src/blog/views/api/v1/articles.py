from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.services import get_current_user
from blog.schemas import Article, ArticleCreate
from blog.services import create_article_db
from core.db import get_async_session
from users.models import User

router_articles_v1 = APIRouter(tags=['articles'])


@router_articles_v1.post('', response_model=ArticleCreate, responses={400: {"description": "Title must be unique"}})
async def create_article(article: ArticleCreate,
                         current_user: User = Depends(get_current_user),
                         db: AsyncSession = Depends(get_async_session)) -> Article:
    article = await create_article_db(current_user, article, db)
    return article
