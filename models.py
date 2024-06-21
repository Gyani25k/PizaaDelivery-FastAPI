from database import Base
from sqlalchemy import Column,Integer,String,Boolean,Text,ForeignKey
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'User_Master'

    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(25),unique=True,nullable=False)
    email = Column(String(255),unique=True,nullable=False)
    password = Column(Text,nullable=False)
    is_active = Column(Boolean,default=True)
    is_staff = Column(Boolean,default=True)
    orders = relationship('Order',back_populates='user')     

class Order(Base):
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