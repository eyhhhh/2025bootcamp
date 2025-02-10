from datetime import datetime, timedelta, timezone
from jose import jwt

SECRET_KEY = "1234"
ALG = "HS256"

class JWTUtil:
  # 1. JWT Token 생성 함수
  # Payload={
  #   "id": 1,
  #   "login_id": "loiss",
  #   "name": "aaaaa"
  # }, 유효기간(default = 30분)
  # -> Jwt token
  
  def create_token(self, payload:dict,
                   expires_delta: timedelta|None = timedelta(minutes=30)):
    payload_to_encode = payload.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    payload_to_encode.update({
      "exp": expire
    })
    return jwt.encode(payload_to_encode, SECRET_KEY, algorithm=ALG)
  
  # 2. token 문자열로 payload 만드는 함수 
  def decode_token(self, token:str) -> dict|None:
    try:
      return jwt.decode(token, SECRET_KEY, algorithms=[ALG])
    except:
      pass
    return None

# 오류 확인해보는 코드 
if __name__ == '__main__':
  payload={
  "id": 1,
  "name": "loiss",
  "login_id": "aaaaa"
  }
  
  jwtUtil = JWTUtil()
  token = jwtUtil.create_token(payload=payload, expires_delta=timedelta(minutes=5))
  print(token)
  
  payload2 = jwtUtil.decode_token(token)