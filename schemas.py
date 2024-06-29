from pydantic import BaseModel
from typing import Optional

class SignupModel(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_active: Optional[bool] = None
    is_staff: Optional[bool] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }


class Settings(BaseModel):
    authjwt_Secret_key:str = '80fa2d91e8a0adea787c23a53c33c6594ac21bf4f601facd7624efa2097539d0'

class LoginModel(BaseModel):
    username:str
    password:str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "password"
            }
        }

class OrderModel(BaseModel):
    id:Optional[int] = None
    quantity:int
    order_status:Optional[str] = "PENDING"
    pizza_size:Optional[str] = "SMALL"
    user_id:Optional[int] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "quantity": 1,
                "order_status": "PENDING",
                "pizza_size":"SMALL",
                "user_id":1
            }
        }

