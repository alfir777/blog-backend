from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from blog.models import Article as ArticleModel
from blog.schemas import Article, ArticleCreate
from users.models import User

error_messages = {
    'unique constraint "ix_articles_title"': "Title must be unique",
    'unique constraint "ix_articles_slug"': "Slug must be unique",
}


async def create_article_db(current_user: User, article: ArticleCreate, db: AsyncSession) -> Article:
    db_article = ArticleModel(**article.model_dump(), author_id=current_user.id)
    db.add(db_article)
    try:
        await db.commit()
    except IntegrityError as e:
        error_message = next((msg for err, msg in error_messages.items() if err in str(e)), "An error occurred")
        raise HTTPException(status_code=400, detail=error_message)
    await db.refresh(db_article)
    return Article.from_orm(db_article)
