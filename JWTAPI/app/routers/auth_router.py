from fastapi import APIRouter, Depends, HTTPException
from app.models.parameter_models import AuthSignupReq
from app.dependencies.db import get_db_session
from app.dependencies.jwt_utils import JWTUtil
from app.services.auth_service import AuthService

router = APIRouter(prefix='/auth')

@router.post('/signup')
def auth_signup(req: AuthSignupReq,
                db=Depends(get_db_session),
                jwtutil: JWTUtil=Depends(JWTUtil),
                authService: AuthService=Depends(AuthService)):
  user = authService.signup(db, req.login_id, req.pwd, req.name)
  if not user:
    raise HTTPException(status_code=400, detail="뭔가 잘못된 부분이 있다.")
  user.access_token = jwtutil.create_token(user.model_dump())
  return user

@router.post('/signin')
def auth_signin():
  pass