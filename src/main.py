from fastapi import FastAPI

from auth.views.api.v1.auth import router_auth_v1
from blog.views.api.v1.articles import router_articles_v1
from users.views.api.v1.users import router_users_v1

app = FastAPI()


app.include_router(
    router_users_v1,
    prefix='/api/v1/users'
)

app.include_router(
    router_articles_v1,
    prefix='/api/v1/articles'
)

app.include_router(
    router_auth_v1,
    prefix='/api/v1/auth'
)


@app.get('/api/v1')
async def root():
    return {'message': 'Hello World'}
