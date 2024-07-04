from fastapi import APIRouter,status,Depends
from database import Session,engine
from schemas import SignupModel,LoginModel
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash,check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter(prefix='/auth',
                        tags=['Authorization'])

session = Session(bind=engine)

@auth_router.get('/')
async def hello(Authorize:AuthJWT=Depends()):
    """
    Returns a message if the token is valid.

    Args:
      Authorize (AuthJWT): The authorization token.

    Raises:
      HTTPException: If the token is invalid.

    Returns:
      dict: A message if the token is valid.

    Examples:
      >>> hello(Authorize)
      {"message":"Hello World"}
    """
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    return {"message":"Hello World"}

@auth_router.post('/signup',response_model=SignupModel,status_code=status.HTTP_201_CREATED)
async def signup(user:SignupModel):
    """
    Creates a new user.

    Args:
      user (SignupModel): The user's information.

    Returns:
      User: The new user.

    Raises:
      HTTPException: If the email or username already exists.

    Examples:
      >>> signup(user)
      User(username, email, password, is_active, is_staff)
    """
    db_email = session.query(User).filter(User.email==user.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="User with the email already exists"
                             
                            )
    
    db_username = session.query(User).filter(User.username==user.username).first()
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="User with the Username already exists"
                             
                            )
    
    new_user = User(
        username = user.username,
        email = user.email,
        password = generate_password_hash(user.password),
        is_active = user.is_active,
        is_staff = user.is_staff
    )

    session.add(new_user)
    session.commit()

    return new_user


@auth_router.post('/login',status_code=200)
async def login(user:LoginModel,Authorize:AuthJWT=Depends()):
    """
    Logs in a user.

    Args:
      user (LoginModel): The user's login information.
      Authorize (AuthJWT): The authorization token.

    Returns:
      dict: The access and refresh tokens.

    Raises:
      HTTPException: If the username or password is invalid.

    Examples:
      >>> login(user, Authorize)
      {"access_token":access_token, "refresh_token":refresh_token}
    """
    db_user = session.query(User).filter(User.username==user.username).first()

    if db_user and check_password_hash(db_user.password,user.password):
        access_token = Authorize.create_access_token(subject=db_user.username)
        refresh_token = Authorize.create_refresh_token(subject=db_user.username)

        response = {
            "access_token":access_token,
            "refresh_token":refresh_token
        }

        return jsonable_encoder(response)
    
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Invalid Username Or Password"
                        )


@auth_router.get('/refresh')
async def refresh_token(Authorize:AuthJWT=Depends()):
    """
    Refreshes the access token.

    Args:
      Authorize (AuthJWT): The authorization token.

    Raises:
      HTTPException: If the refresh token is invalid.

    Returns:
      dict: The new access token.

    Examples:
      >>> refresh_token(Authorize)
      {"access":access_token}
    """
    try:
        Authorize.jwt_refresh_token_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please provide a valid refresh token"
        ) 

    current_user=Authorize.get_jwt_subject()

    
    access_token=Authorize.create_access_token(subject=current_user)

    return jsonable_encoder({"access":access_token})