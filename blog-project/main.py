from fastapi import FastAPI
from enum import Enum
from dataclasses import dataclass
import time

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

@dataclass
class AuthLoginReq:
  login_id: str
  password: str
  
@dataclass
class AuthResponse:
  jwt_token: str | None=None 
  err_msg: str | None=None

@app.post('/auth/signup')
def signup(user: User)->AuthResponse:
  return AuthResponse(
    jwt_token="dsdkfdkfj"
  )

@app.post('/auth/signin')
def signin(user: AuthLoginReq)->AuthResponse:
  return AuthResponse(
    jwt_token= "aaaa"
  )
  
@app.get('/posts')
def get_posts():