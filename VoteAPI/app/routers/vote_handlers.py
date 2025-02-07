from fastapi import APIRouter, Depends
from app.services.vote_service import VoteService
from app.depedencies.redis_db import get_redis

router = APIRouter(prefix='/v1/vote')

@router.get('/members')
def get_members(service=Depends(VoteService)): # 의존성 주입?
  members = service.members()
  return members

@router.put('/{member_id}') # /v1/vote
async def vote(member_id: int, 
               service=Depends(VoteService),
               redis=Depends(get_redis)):
  service.vote(redis, member_id)
  return {}