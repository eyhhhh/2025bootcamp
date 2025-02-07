from pydantic import BaseModel, ValidationError, conint, SecretStr
from typing import Optional, Literal, Callable
import json
from datetime import date, datetime, time, timedelta

class Addr:
  country: str
  city: str
  
class User(BaseModel):
  id: int
  name: str
  email: str
  is_active: bool=True
  addr: Optional[Addr] = None # 생략가능하다는 뜻

class Shop(BaseModel):
  id: int
  name: str
  addr: Addr


user = User(id=1, name="Song", email="email@example.com", is_active=True)
print(user.model_dump_json())

user_dict = user.model_dump()
print(user_dict)

userDict = {
  "id": 99,
  "name": "Linux",
  "email": "linux@linux.com",
  "is_active": False
}

user4 = User(**userDict) # 함수 안에서 풀어서 사용

strJson = '{"id": 10,"name": "email","email": "email@email.com","is_active": False}'
user5 = User.model_validate_json(strJson)

class Switch(BaseModel):
  on: bool

s1 = Switch(on=True)
s2 = Switch(on='on')

class Methods(BaseModel):
  on_strap: Callable[[int],str]

def int_to_str(val: int)->str:
  return f'{val}'

m = Methods(on_strap=int_to_str)
m.on_strap(100)

class TestModel(BaseModel):
  age: conint(gt=15, lt=150)
  
try:
  print(TestModel(age=20))
  print(TestModel(age=200))
except Exception as e:
  print(e)
  
class SecretUser(BaseModel):
  login_id: str
  pwd: SecretStr
  
sUser = SecretUser(login_id='abcd', pwd='1234')
if sUser.pwd == '1234':
  print(True)
else:
  print(False)