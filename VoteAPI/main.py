from fastapi import FastAPI, Depends, Path
from app.routers import vote_handlers

app = FastAPI()
app.include_router(vote_handlers)

