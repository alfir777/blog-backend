import os

DB_HOST = os.environ.get('DB_HOST', '')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'blog')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_USER = os.environ.get('DB_USER', 'user')

if DB_HOST:
    POSTGRES_ASYNC_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
else:
    POSTGRES_ASYNC_URL = 'sqlite:///./databe.db'
