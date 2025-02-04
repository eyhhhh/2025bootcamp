from fastapi import FastAPI
from enum import Enum
from dataclasses import dataclass

# 서버 생성
app = FastAPI()

@dataclass
class User:
  login_id: str
  password: str
  name: str

@dataclass
class Post:
  id: int
  title: str
  body: str
  created_at: int
  published: bool
  
@app.post('/auth/signup')
def signup():
  