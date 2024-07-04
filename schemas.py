from pydantic import BaseModel
from typing import Optional

class SignupModel(BaseModel):
    """
    Model for user signup.

    Attributes:
      id (int, optional): The unique identifier for the user.
      username (str): The username for the user.
      email (str): The email address for the user.
      password (str): The password for the user.
      is_active (bool, optional): Whether the user is active or not.
      is_staff (bool, optional): Whether the user is a staff member or not.

    Config:
      orm_mode (bool): Whether to use ORM mode or not.
      schema_extra (dict): Extra schema information for the model.

    Example:
      >>> SignupModel(
      ...     username="johndoe",
      ...     email="johndoe@gmail.com",
      ...     password="password",
      ...     is_staff=False,
      ...     is_active=True
      ... )
      SignupModel(id=None, username='johndoe', email='johndoe@gmail.com', password='password', is_active=True, is_staff=False)
    """
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_active: Optional[bool] = None
    is_staff: Optional[bool] = None

    class Config:
        """
      orm_mode (bool): Whether to use ORM mode or not.
      schema_extra (dict): Extra schema information for the model.

    Example:
      >>> SignupModel(
      ...     username="johndoe",
      ...     email="johndoe@gmail.com",
      ...     password="password",
      ...     is_staff=False,
      ...     is_active=True
      ... )
      SignupModel(id=None, username='johndoe', email='johndoe@gmail.com', password='password', is_active=True, is_staff=False)
    """
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
    """
    Model for application settings.

    Attributes:
      authjwt_Secret_key (str): The secret key for authentication.
    """
    authjwt_Secret_key:str = '80fa2d91e8a0adea787c23a53c33c6594ac21bf4f601facd7624efa2097539d0'

class LoginModel(BaseModel):
    """
    Model for user login.

    Attributes:
      username (str): The username for the user.
      password (str): The password for the user.

    Config:
      orm_mode (bool): Whether to use ORM mode or not.
      schema_extra (dict): Extra schema information for the model.

    Example:
      >>> LoginModel(
      ...     username="johndoe",
      ...     password="password"
      ... )
      LoginModel(username='johndoe', password='password')
    """
    username:str
    password:str

    class Config:
        """
      orm_mode (bool): Whether to use ORM mode or not.
      schema_extra (dict): Extra schema information for the model.

    Example:
      >>> SignupModel(
      ...     username="johndoe",
      ...     email="johndoe@gmail.com",
      ...     password="password",
      ...     is_staff=False,
      ...     is_active=True
      ... )
      SignupModel(id=None, username='johndoe', email='johndoe@gmail.com', password='password', is_active=True, is_staff=False)
    """
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "password"
            }
        }

class OrderModel(BaseModel):
    """
    Model for pizza orders.

    Attributes:
      id (int, optional): The unique identifier for the order.
      quantity (int): The quantity of pizzas in the order.
      order_status (str, optional): The status of the order.
      pizza_size (str, optional): The size of the pizza in the order.
      user_id (int, optional): The unique identifier for the user who placed the order.

    Config:
      orm_mode (bool): Whether to use ORM mode or not.
      schema_extra (dict): Extra schema information for the model.

    Example:
      >>> OrderModel(
      ...     quantity=1,
      ...     order_status="PENDING",
      ...     pizza_size="SMALL",
      ...     user_id=1
      ... )
      OrderModel(id=None, quantity=1, order_status='PENDING', pizza_size='SMALL', user_id=1)
    """
    id:Optional[int] = None
    quantity:int
    order_status:Optional[str] = "PENDING"
    pizza_size:Optional[str] = "SMALL"
    user_id:Optional[int] = None

    class Config:
        """
      orm_mode (bool): Whether to use ORM mode or not.
      schema_extra (dict): Extra schema information for the model.

    Example:
      >>> SignupModel(
      ...     username="johndoe",
      ...     email="johndoe@gmail.com",
      ...     password="password",
      ...     is_staff=False,
      ...     is_active=True
      ... )
      SignupModel(id=None, username='johndoe', email='johndoe@gmail.com', password='password', is_active=True, is_staff=False)
    """
        orm_mode = True
        schema_extra = {
            "example": {
                "quantity": 1,
                "order_status": "PENDING",
                "pizza_size":"SMALL",
                "user_id":1
            }
        }

class OrderStatusModel(BaseModel):
    """
    Model for updating the status of an order.

    Attributes:
      order_status (str, optional): The new status for the order.

    Config:
      orm_mode (bool): Whether to use ORM mode or not.
      schema_extra (dict): Extra schema information for the model.

    Example:
      >>> OrderStatusModel(
      ...     order_status="PENDING"
      ... )
      OrderStatusModel(order_status='PENDING')
    """
    order_status:Optional[str] = "PENDING"

    class Config:
        """
      orm_mode (bool): Whether to use ORM mode or not.
      schema_extra (dict): Extra schema information for the model.

    Example:
      >>> SignupModel(
      ...     username="johndoe",
      ...     email="johndoe@gmail.com",
      ...     password="password",
      ...     is_staff=False,
      ...     is_active=True
      ... )
      SignupModel(id=None, username='johndoe', email='johndoe@gmail.com', password='password', is_active=True, is_staff=False)
    """
        orm_mode = True
        schema_extra = {
            "example": {
                "order_status": "PENDING"
            }
        }
