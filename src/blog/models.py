from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import backref, relationship

from core.db import Base


article_tags = Table(
    'article_tags',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('articles.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True, index=True)
    description = Column(String, nullable=True)
    slug = Column(String, nullable=False, unique=True, index=True)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    author = relationship('User', backref='articles')
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    photo = Column(String, nullable=True)
    views = Column(Integer, default=0, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    category = relationship('Category', backref='articles')
    tags = relationship('Tag', secondary=article_tags, backref='articles')
    votes = Column(Integer, default=0, nullable=False)
    likes = Column(Integer, default=0, nullable=False)
    dislikes = Column(Integer, default=0, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship('Article', backref='comments')
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', backref='comments')
    parent_id = Column(Integer, ForeignKey('comments.id'))
    parent = relationship('Comment', backref=backref('children', remote_side=[id]))
    votes = Column(Integer, default=0, nullable=False)
    likes = Column(Integer, default=0, nullable=False)
    dislikes = Column(Integer, default=0, nullable=False)


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    slug = Column(String, nullable=False, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    slug = Column(String, nullable=False, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    parent_id = Column(Integer, ForeignKey('categories.id'))
    parent = relationship('Category', backref=backref('children', remote_side=[id]))
    te = Column(String, nullable=False)
