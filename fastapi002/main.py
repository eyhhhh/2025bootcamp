from fastapi import FastAPI
from app.handlers import auth_handlers
from app.handlers import posts_handlers
from app.dependencies import get_db_session, create_db
# 서버 생성
app = FastAPI()

app.include_router(auth_handlers.router)
app.include_router(posts_handlers.router)

@app.on_event("startup")
def on_startup():
  create_db()