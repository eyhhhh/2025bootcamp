from dataclasses import dataclass
from fastapi import APIRouter

router = APIRouter(
  prefix="/v1/auth" # 모든 경로 앞에 추가
)

@dataclass
class User:
  login_id: str
  password: str
  name: str
  
@dataclass
class AuthLoginReq:
  login_id: str
  password: str
  
@dataclass
class AuthResponse:
  jwt_token: str | None=None 
  err_msg: str | None=None
  
  
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