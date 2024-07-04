from fastapi import APIRouter,Depends,status
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from models import User,Order
from schemas import OrderModel,OrderStatusModel
from database import engine,Session
from fastapi.encoders import jsonable_encoder


order_router = APIRouter(prefix='/order',
                         tags=['Orders'])

session = Session(bind=engine)

@order_router.get('/')
async def hello(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    return {"message":"Hello World "}


@order_router.post('/order',status_code=status.HTTP_201_CREATED)
async def place_an_order(order:OrderModel,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user = Authorize.get_jwt_subject()

    user= session.query(User).filter(User.username==current_user).first()

    new_order = Order(
        pizza_size=order.pizza_size,
        quantity = order.quantity
    )

    new_order.user = user

    session.add(new_order)

    session.commit()

    response = {
       "pizza_size":new_order.pizza_size,
       "quantity":new_order.quantity,
       "id":new_order.id,
       "order_status":new_order.order_status 
    }

    return jsonable_encoder(response)


@order_router.get('/order',status_code=status.HTTP_200_OK)
async def get_all_orders(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user = Authorize.get_jwt_subject()

    user= session.query(User).filter(User.username==current_user).first()

    if user.is_staff:
        orders = session.query(Order).all()

        return jsonable_encoder(orders)
    
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not a Superuser"
    )

@order_router.get('/order/{id}',status_code=status.HTTP_200_OK)
async def get_order_based_on_user_id(id:int,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user = Authorize.get_jwt_subject()

    user= session.query(User).filter(User.username==current_user).first()

    if user.is_staff:
        orders = session.query(Order).filter(Order.id==id).first()

        return jsonable_encoder(orders)
    
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not a Superuser"
    )


@order_router.get('/user/order',status_code=status.HTTP_200_OK)
async def get_current_users_order(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user = Authorize.get_jwt_subject()

    user= session.query(User).filter(User.username==current_user).first()

    orders = session.query(Order).filter(Order.user_id==user.id).first()

    return jsonable_encoder(orders)

@order_router.get('/user/order/{id}',status_code=status.HTTP_200_OK,response_model=OrderModel)
def get_current_users_order(id:int,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user = Authorize.get_jwt_subject()

    user= session.query(User).filter(User.username==current_user).first()

    orders = user.orders

    for order in orders:
        if order.id == id:
            return order
        
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="No order with this id found")


@order_router.get('/order/update/{id}',status_code=status.HTTP_200_OK)
def update_order(id:int,order:OrderModel,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user = Authorize.get_jwt_subject()

    order_to_update = session.query(Order).filter(Order.id==id).first()

    order_to_update.quantity = order.quantity
    order_to_update.pizza_size = order.pizza_size

    session.commit()

    return jsonable_encoder(order_to_update)


@order_router.patch('/order/update/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update_order_status(id:int,order:OrderStatusModel,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user = Authorize.get_jwt_subject()

    user= session.query(User).filter(User.username==current_user).first()

    if user.is_staff:
        order_to_update = session.query(Order).filter(Order.id==id).first()
        order_to_update.order_status = order.order_status

        session.commit()

        return jsonable_encoder(order_to_update)
    
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not a Superuser"
    )

@order_router.delete('/order/delete/{id}/',status_code=status.HTTP_204_NO_CONTENT)
async def delete_an_order(id:int,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Token")


    order_to_delete=session.query(Order).filter(Order.id==id).first()

    session.delete(order_to_delete)

    session.commit()

    return order_to_delete



