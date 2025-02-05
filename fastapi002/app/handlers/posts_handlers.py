import time
from fastapi import APIRouter, Depends, HTTPException
from app.models.post import *
from app.models.shared import *
from app.dependencies import get_db_session
from sqlmodel import select
from dataclasses import asdict 

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
  db.refresh(postModel) # db에 삽입된 값을 불러오는 것
  return postModel
  
# 게시물 목록
@router.get('/')
def get_posts(page: int=1, limit: int=2, db=Depends(get_db_session)) -> PostResp:
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
  
  resp = PostResp(posts = posts)
  return resp


# 게시물 보기
@router.get('/{post_id}')
def get_post(post_id: int, db=Depends(get_db_session))->PostResp:
  post = db.get(Post, post_id)
  if not post:
    raise HTTPException(status_code=404, detail="Not Found")
  
  resp = PostResp(posts=[post])
  return resp


# 게시물 수정
@router.put('/{post_id}') # or PATCH
def update_post(post_id: int, reqBody: PostReq,
                db=Depends(get_db_session)):
  oldPost = db.get(Post,post_id)
  if not oldPost:
    raise HTTPException(status_code=404, detail="Post not found")
  
  dicToUpdate = asdict(reqBody) # 딕셔너리로 변환
  oldPost.sqlmodel_update(dicToUpdate)
  db.add(oldPost)
  db.commit() # 꼭 해주기
  db.refresh(oldPost)  
  
  return oldPost


# 게시물 삭제
@router.delete('/{post_id}')
def delete_post(post_id: int, db=Depends(get_db_session)):
  post = db.get(Post, post_id)
  if not post:
    raise HTTPException(status_code=404, detail="Post not found")
  db.delete(post)
  db.commit() # 트랜잭션 종료
  
  return {'ok': True}