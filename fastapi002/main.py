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

class PageDir(Enum):
  NEXT = "next"
  PREV = "prev"

@dataclass
class PostsResp:
  posts: list[Post]
  err_msg: str | None = None

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
def get_posts(dir: PageDir=PageDir.PREV,
              post_id: int=0,
              limit: int=30) -> PostsResp:
  now = int(time.time())
  return PostsResp(
    posts = [
      Post(id=1, title="T1", created_at=now, published=True),
      Post(id=2, title="T2", created_at=now, published=True)
    ]
  )
  
@app.get('/posts/{post_id}')
def get_posts(post_id: int) -> PostsResp:
  now = int(time.time())
  return PostsResp(
    posts = [
      Post(id=post_id, title="T3", created_at=now, published=True)
    ]
  )