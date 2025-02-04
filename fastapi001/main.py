from fastapi import FastAPI
from enum import Enum
from dataclasses import dataclass

# 서버 생성
app = FastAPI()

@app.get("/")
def root():
  return {"message": "Hello, World!"}


# Path Parameter

@app.get("/products/first")
def get_first_product():
  return {"name": "Product 1"}  

@app.get("/products/{product_id}")
def get_product(product_id: int):
  return {
    "products": [
        {"id": product_id, "name": "Product 1"},
      ]
    }

class CarTypes(str, Enum):
  Truck = "truck"
  Sedan = "sedan"
  SUV = "suv"
  
@app.get("/cars/{car_type}")
def get_car(car_type: CarTypes):
  return {"car_type": car_type}

# Query Parameter
@app.get("/products")
def get_products(q: str | None = None):
  products = {"products": [{"name": "Product 1"}, {"name": "Product2"}]}
  if q:
    products.update({"q": q})
  return products

# Request Body
@dataclass
class RequestLogin:
  login_id: str
  password: str

@app.post("/auth/login")
def login(req: RequestLogin):
  return req

@dataclass
class RespUser:
  id: int
  name: str
  age: int
  email: str
  
@app.get("/users/{user_id}")
def get_user_profile(user_id: int) -> RespUser:
  return RespUser(id=user_id, name="Song", age=40, email="")