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
