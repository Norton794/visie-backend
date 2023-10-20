from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from app.routes import router
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_url = os.getenv("DB_URL")

register_tortoise(
    app,
    db_url=db_url,
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(router, prefix="/api")
