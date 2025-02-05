from dataclasses import dataclass
from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel

class PageDir(Enum):
  NEXT = "next"
  PREV = "prev"

@dataclass
class Post(SQLModel, table=True):
  id: int | None = Field(primary_key=True)
  title: str
  body: str
  created_at: int = Field(index=True)
  published: bool = Field(index=True)
  

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
