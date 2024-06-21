from fastapi import FastAPI
from auth import auth_router
from order import order_router

app=FastAPI()

app.include_router(auth_router)
app.include_router(order_router)

