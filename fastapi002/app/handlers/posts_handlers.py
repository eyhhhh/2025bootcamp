import time
from fastapi import APIRouter, Depends, HTTPException
from app.models.post import *
from app.models.shared import *
from app.dependencies import get_db_session
from sqlmodel import select


router = APIRouter(
  prefix="/v1/posts" # 모든 경로 앞에 추가
)

# 게시물 등록
@router.post('/')
def create_post(post: PostReq, db = Depends(get_db_session)):
  postModel = Post()
  postModel.title = post.title
  postModel.body = post.body
  postModel.created_at = int(time.time())
  postModel.published = post.published
  db.add(postModel)
  db.commit()
  db.refresh(postModel)
  return postModel
  
# 게시물 목록
@router.get('/')
def get_posts(page: int=1, limit: int=2, db=Depends(get_db_session)):
  if page < 1:
    page = 1
  if limit < 1:
    return []
  if limit > 2:
    limit = 2
    
  nOffset = (page-1) * limit
  posts = db.exec(
    select(Post).offset(nOffset).limit(limit)
  ).all()
  
  return posts

# 게시물 보기
@router.get('/{post_id}')
def get_post(post_id: int, db=Depends(get_db_session)):
  post = db.get(Post, post_id)
  if not post:
    raise HTTPException(status_code=404, detail="Not Found")
  return [post]


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