from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  created_at: int | None = Field(index=True)
  login_id: str = Field(index=True)
  pwd: str = Field(default=None, exclude=True) # json변환시 배제해라
  name: str
  access_token: str|None = None