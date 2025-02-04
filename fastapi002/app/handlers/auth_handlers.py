from fastapi import APIRouter
from app.models.user import *

router = APIRouter(
  prefix="/v1/auth" # 모든 경로 앞에 추가
)

# 회원가입
@router.post('/signup')
def signup(user: User)->AuthResponse:
  return AuthResponse(
    jwt_token="dsdkfdkfj"
  )

# 로그인
@router.post('/signin')
def signin(user: AuthLoginReq)->AuthResponse:
  return AuthResponse(
    jwt_token= "aaaa"
  )