from fastapi import FastAPI
from app.dependencies.db import create_db_and_table
from app.routers import auth_router

create_db_and_table()

app = FastAPI()
app.include_router(auth_router.router)