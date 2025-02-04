from enum import Enum
from dataclasses import dataclass
import time
from typing import Optional
from fastapi import APIRouter

router = APIRouter(
  prefix="/v1/posts" # 모든 경로 앞에 추가
)

class PageDir(Enum):
  NEXT = "next"
  PREV = "prev"

@dataclass
class Post:
  id: int
  title: str
  body: str
  created_at: int
  published: bool

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
  
  
  
# 게시물 목록
@router.get('/')
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
@router.get('/{post_id}')
def get_posts(post_id: int) -> PostsResp:
  now = int(time.time())
  return PostsResp(
    posts = [
      Post(id=post_id, title="T3", created_at=now, published=True)
    ]
  )

# 게시물 등록
@router.post('/')
def create_post(params: CreatePostReq) -> PostsResp:
  now = int(time.time())
  return PostsResp(
    posts = [
      Post(id=4, title=params.title, body=params.body, created_at=now, published=params.publish)
    ]
  )

# 게시물 수정
@router.post('/{post_id}')
def update_post(post_id: int, params: UpdatePostReq) -> PostsResp:
  now = int(time.time())
  return PostsResp(
    posts = [
      Post(id=post_id, title=params.title, body=params.body, created_at=now, published=params.publish)
    ]
  )

# 게시물 삭제
@router.delete('/{post_id}')
def delete_post(post_id: int) -> dict:
  return(
    ResultReq(ok=True)
  )