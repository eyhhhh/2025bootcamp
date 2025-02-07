from fastapi import APIRouter, Depends, Path, HTTPException
from app.services.vote_service import VoteService
from app.depedencies.redis_db import get_redis
from typing import Annotated


router = APIRouter(prefix='/v1/vote')

@router.get('/members')
def get_members(service=Depends(VoteService)): # 의존성 주입?
  members = service.members()
  return members

@router.put('/{member_id}/{phone}') # /v1/vote
async def vote(member_id: Annotated[int, Path(ge=0, le=2)],  # Path parameter검증
               phone: str,
               service=Depends(VoteService),
               redis=Depends(get_redis)):
  if member_id not in [0,1,2]:
    raise HTTPException(status_code=400, detail="0-1")
  await service.vote(redis, member_id)
  
  if await service.phone_exists(redis, phone):
    raise HTTPException(status_code=401, detail="이미 투표하셨습니다.")
  
  await service.set_phone(redis, phone)
  
  return {}

@router.get('/') # v1/vote
async def get_scores(service=Depends(VoteService), redis=Depends(get_redis)):
  scores=await service.score(redis)
  return scores