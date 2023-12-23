import uvicorn

from fastapi import FastAPI
from fastapi_pagination import add_pagination
from contextlib import asynccontextmanager

from core.config import settings
from api_v1 import router as router_v1

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

def create_app():
    app = FastAPI(lifespan=lifespan,title='Hotel REST API')
    
    add_pagination(app)

    app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
    return app

if __name__ == '__main__':
    uvicorn.run('main:create_app', factory=True, reload=True, port=8000)