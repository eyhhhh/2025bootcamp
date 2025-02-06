from fastapi import FastAPI
from app.handlers import auth_handlers
from app.handlers import posts_handlers
from app.dependencies import get_db_session, create_db
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DB_HOST")
db_pwd = os.getenv("DB_PASS")

# 서버 생성
app = FastAPI()

app.include_router(auth_handlers.router)
app.include_router(posts_handlers.router)

@app.on_event("startup")
def on_startup():
  create_db()