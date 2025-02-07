from fastapi import (
    APIRouter,HTTPException,Depends
)
from app.models.post_models import *
from app.dependencies.sqlite_db import *
from app.dependencies.redis_db import get_redis
from app.services.post_service import PostService
from app.services.redis_service import RedisService

router = APIRouter()

@router.post("/posts")
def create_post(post: PostReq,
                db = Depends(get_db_session),
                postService: PostService = Depends()):
    resp = postService.create_post(db, post)

    return resp

@router.get("/posts")
def get_posts(page: int=1, 
            db=Depends(get_db_session),
            postService: PostService = Depends()) -> PostResp:
    if page < 1:
        page = 1
    resp = PostResp(posts=[])
    resp.posts = postService.get_posts(db, page)
    return resp

@router.get("/posts/{post_id}")
async def get_post(post_id: int, 
            db=Depends(get_db_session), # 의존성 주입 
            redis=Depends(get_redis),
            postService: PostService = Depends(),
            redisService=Depends(RedisService)) -> PostResp:
    
    cachedPost = redisService.get_post(redis, post_id)
    if cachedPost is not None:
      return PostResp([cachedPost])
    
    post = postService.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404,
                            detail="Not Found")
        
    # add cache
    await redisService.add_post(redis, post)
    
    resp = PostResp(posts=[post])
    return resp

@router.delete("/posts/{post_id}")
async def delete_post(post_id: int,
            db=Depends(get_db_session),
            redis=Depends(get_redis),
            postService: PostService = Depends(),
            redisService=Depends(RedisService)):
    
    resultCode = postService.delete_post(db, post_id)
    if resultCode == RESULT_CODE.NOT_FOUND:
        raise HTTPException(status_code=404,
                            detail="not found")
    
    await redisService.delete_post(redis, post_id)
    
    return {
        'ok': True
    }

@router.put("/posts/{post_id}")
def update_post(post_id:int, 
            reqBody: PostReq,
            db=Depends(get_db_session),
            redis=Depends(get_redis),
            postService: PostService = Depends(),
            redisService=Depends(RedisService)):
    post, code = postService.update_post(db, post_id, reqBody)
    if code == RESULT_CODE.NOT_FOUND:
        raise HTTPException(status_code=404,
                            detail="not found")
    if code == RESULT_CODE.FAILED:
        raise HTTPException(status_code=500,
                            detail="internal server error")
        
    redisService.update_post(redis, post_id)
    
    return post





