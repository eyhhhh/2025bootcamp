from fastapi import FastAPI,HTTPException,status,Depends
from dataclasses import dataclass

app = FastAPI()

def get_notices_form_db():
  return ['공지사항입니다', '긴급공지입니다']

@app.get('/')
def home():
  noticeList = get_notices_form_db()
  
  return{
    "name":"Linux",
    "notices": noticeList
  }


@dataclass
class SigninReq:
  login_id: str
  password: str
  

def validate_signin_req(req: SigninReq) -> SigninReq:
  if len(req.login_id) < 1:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail='Length of password: 4-12'
    )
  return req

@app.post('/auth/login')
def auth_login(user: SigninReq=Depends(validate_signin_req)):
  # user = validate_signin_req(user)
  return user