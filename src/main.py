import uvicorn

from core.config import settings
from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

def create_app():
    app = FastAPI(lifespan=lifespan,title='Hotel REST API')
    return app

if __name__ == '__main__':
    uvicorn.run('main:create_app', factory=True, reload=True, port=8000)