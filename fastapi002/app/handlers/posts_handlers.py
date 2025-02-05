import time
from fastapi import APIRouter, Depends
from app.models.post import *
from app.models.shared import *
from app.dependencies import get_db_session


router = APIRouter(
  prefix="/v1/posts" # 모든 경로 앞에 추가
)

@router.post('/')
def create_post(post: Post, db = Depends(get_db_session)):
  post.created_at = int(time.time())
  db.add(post)
  db.commit()
  db.refresh(post)
  return post
  
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
    ResultResp(ok=True)
  )