from sqlmodel import Session,select
from dataclasses import dataclass,asdict
from sqlmodel import (SQLModel, Session, Field)
import time
from enum import Enum

class RESULT_CODE(Enum):
  SUCCESS = 1
  NOT_FOUND = -2
  FAILED = -3

@dataclass
class PostReq:
  title: str
  body: str
  published: bool
  
  
# db 작업시 사용
class Post(SQLModel, table=True):
  id: int = Field(primary_key=True) # unique해야함
  created_at: int = Field(index=True)
  published: bool = Field(index=True)
  title: str
  body: str
  

class PostService:
  def get_post(self, db: Session, post_id: int):
    post = db.get(Post, post_id)
    return post
  
  def get_posts(self, db: Session, page: int=1, limit: int=10):
    # 중복 검증
    if limit > 10:
      limit = 10
    
    nOffset = (page-1) * limit # 10개씩 가져옴
    posts = db.exec(
      select(Post).offset(nOffset).limit(limit)
    ).all()
    
    return posts
  
  def create_post(self, db: Session, post: PostReq):
    postModel = Post()
    postModel.title = post.title
    postModel.body = post.body
    postModel.created_at = int(time.time())
    postModel.published = post.published
    db.add(postModel)
    db.commit()
    db.refresh(postModel) # db에 삽입된 값을 불러오는 것
    return postModel
  
  def update_post(self, db: Session, post_id: int, post: PostReq)-> tuple[Post|None,RESULT_CODE]:
    oldPost = db.get(Post,post_id)
    if not oldPost:
      return (None, RESULT_CODE.NOT_FOUND)
    
    dicToUpdate = asdict(post) # 딕셔너리로 변환
    oldPost.sqlmodel_update(dicToUpdate)
    try:
      db.add(oldPost)
      db.commit() # 꼭 해주기
      db.refresh(oldPost)  
    except:
      return (None, RESULT_CODE.FAILED)
    return (oldPost, RESULT_CODE.SUCCESS)
  
  def delete_post(self, db: Session, post_id: int)->RESULT_CODE:
    post = db.get(Post, post_id)
    if not post:
      raise RESULT_CODE.NOT_FOUND
    try:
      db.delete(post)
      db.commit() # 트랜잭션 종료
    except:
      return RESULT_CODE.FAILED
    return RESULT_CODE.SUCCESS # delete가 안돼도 True일 가능성 있음