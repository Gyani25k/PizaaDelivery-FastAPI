from database import Base
from sqlalchemy import Column,Integer,String,Boolean,Text,ForeignKey
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

class User(Base):
    """
    Represents a user in the database.

    Attributes:
      id (int): The unique identifier for the user.
      username (str): The username for the user.
      email (str): The email address for the user.
      password (str): The password for the user.
      is_active (bool): Indicates if the user is currently active.
      is_staff (bool): Indicates if the user has staff privileges.
      orders (list): A list of orders associated with the user.
    """
    __tablename__ = 'User_Master'

    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(25),unique=True,nullable=False)
    email = Column(String(255),unique=True,nullable=False)
    password = Column(Text,nullable=False)
    is_active = Column(Boolean,default=True)
    is_staff = Column(Boolean,default=True)
    orders = relationship('Order',back_populates='user')     

class Order(Base):
    """
    Represents an order in the database.

    Attributes:
      id (int): The unique identifier for the order.
      quantity (int): The quantity of pizzas in the order.
      order_status (str): The current status of the order.
      pizza_size (str): The size of the pizza in the order.
      user_id (int): The id of the user who placed the order.
      user (User): The user who placed the order.

    Notes:
      The order_status and pizza_size attributes are set to default values if not specified.

    Examples:
      >>> order = Order(quantity=2, user_id=1)
      >>> order.pizza_size
      'SMALL'
      >>> order.order_status
      'PENDING'
    """
    __tablename__ = 'Order_Master'

    ORDER_STATUSES = (
        ('PENDING','pending'),
        ('IN-TRANSIT','in-transit'),
        ('DELIVERED','delivered')
    )

    PIZZA_SIZES = (
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large'),
        ('EXTRA-LARGE','extra-large')
    )

    id = Column(Integer,primary_key=True,autoincrement=True)
    quantity = Column(Integer,nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES),default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES),default="SMALL")
    user_id = Column(Integer,ForeignKey('User_Master.id'))
    user = relationship('User',back_populates='orders')