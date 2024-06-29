from fastapi import APIRouter,Depends,status
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from models import User,Order
from schemas import OrderModel
from database import Session

order_router = APIRouter(prefix='/order',
                         tags=['Orders'])


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


@order_router.post('/order')
async def place_an_order(order:OrderModel,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user = Authorize.get_jwt_subject()

