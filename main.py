from fastapi import FastAPI
from auth import auth_router
from order import order_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings

app=FastAPI()

@AuthJWT.load_config
def get_config():
    """
    Loads the configuration settings for the app.

    Returns:
      Settings: The configuration settings for the app.
    """
    return Settings()

app.include_router(auth_router)
app.include_router(order_router)

