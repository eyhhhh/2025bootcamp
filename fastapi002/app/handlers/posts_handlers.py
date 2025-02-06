from fastapi import APIRouter, Depends, HTTPException
from app.models.post import *
from app.models.shared import *
from app.dependencies import get_db_session
from sqlmodel import select
from dataclasses import asdict 
from app.services.post_service import *

router = APIRouter(
  prefix="/v1/posts" # 모든 경로 앞에 추가
)

# 게시물 등록
@router.post('/')
def create_post(post: PostReq, db = Depends(get_db_session), postService: PostService = Depends()):
  return postService.create_post(db, post)

  
# 게시물 목록
@router.get('/')
def get_posts(page: int=1, limit: int=10, db=Depends(get_db_session), 
              postService: PostService = Depends()) -> PostResp:
  if limit > 10:
      limit = 10
      
  resp = PostResp(posts=[])
  resp.posts = postService.get_posts(db, page, limit)
  return resp


# 게시물 보기
@router.get('/{post_id}')
def get_post(post_id: int, db=Depends(get_db_session),
              postService: PostService = Depends())->PostResp:
  post = postService.get_post(db, post_id)
  if not post:
    raise HTTPException(status_code=404, detail="Not Found")
  
  resp = PostResp(posts=[post])
  return resp


# 게시물 수정
@router.put('/{post_id}') # or PATCH
def update_post(post_id: int, reqBody: PostReq,
                db=Depends(get_db_session), postService: PostService = Depends()):
  post,resultCode = postService.update_post(db, post_id, reqBody)
  
  if resultCode == RESULT_CODE.NOT_FOUND:
    raise HTTPException(status_code=404, detail="Post not found")
  if resultCode == RESULT_CODE.FAILED:
    raise HTTPException(status_code=500, detail="Internal server error")
  
  return post


# 게시물 삭제
@router.delete('/{post_id}')
def delete_post(post_id: int, db=Depends(get_db_session),
                postService: PostService = Depends()):
  resultCode = postService.delete_post(db, post_id)
  
  if resultCode == RESULT_CODE.NOT_FOUND:
    raise HTTPException(status_code=404, detail="Post not found")
  if resultCode == RESULT_CODE.FAILED:
    raise HTTPException(status_code=500, detail="Internal server error")
  
  return {'ok': True}