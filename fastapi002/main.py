from fastapi import FastAPI
from enum import Enum
from dataclasses import dataclass
import time
from typing import Optional

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

@dataclass
class CreatePostReq:
  title: str
  body: str
  publish: bool=False
  
@dataclass
class UpdatePostReq:
  title: Optional[str] = None # str | None
  body: Optional[str] = None
  publish: Optional[bool] = None

@dataclass
class ResultReq:
  ok: bool=False
  err_msg: Optional[str]=None
  
  
  
# 회원가입
@app.post('/auth/signup')
def signup(user: User)->AuthResponse:
  return AuthResponse(
    jwt_token="dsdkfdkfj"
  )

# 로그인
@app.post('/auth/signin')
def signin(user: AuthLoginReq)->AuthResponse:
  return AuthResponse(
    jwt_token= "aaaa"
  )
  
# 게시물 목록
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

# 게시물 보기
@app.get('/posts/{post_id}')
def get_posts(post_id: int) -> PostsResp:
  now = int(time.time())
  return PostsResp(
    posts = [
      Post(id=post_id, title="T3", created_at=now, published=True)
    ]
  )

# 게시물 등록
@app.post('/posts')
def create_post(params: CreatePostReq) -> PostsResp:
  now = int(time.time())
  return PostsResp(
    posts = [
      Post(id=4, title=params.title, body=params.body, created_at=now, published=params.publish)
    ]
  )

# 게시물 수정
@app.post('/posts/{post_id}')
def update_post(post_id: int, params: UpdatePostReq) -> PostsResp:
  now = int(time.time())
  return PostsResp(
    posts = [
      Post(id=post_id, title=params.title, body=params.body, created_at=now, published=params.publish)
    ]
  )

# 게시물 삭제
@app.delete('/posts/{post_id}')
def delete_post(post_id: int) -> dict:
  return(
    ResultReq(ok=True)
  )