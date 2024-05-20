from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ArticleBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str = "The title of the article"
    content: str
    slug: str


class ArticleCreate(ArticleBase):
    is_active: bool = Field(default=False)


class Article(ArticleBase):
    key: int | None = Field(default=None, alias='id')
    created_at: datetime | None = Field(default=None)
    updated_at: datetime | None = Field(default=None)
    is_active: bool
    # author_id: int
