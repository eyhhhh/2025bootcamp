from dataclasses import dataclass
from enum import Enum
from typing import Optional
from app.services.post_service import *

class PageDir(Enum):
  NEXT = "next"
  PREV = "prev"

@dataclass
class PostResp:
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
