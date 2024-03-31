from bcrypt import checkpw
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_mail import FastMail, ConnectionConfig, MessageSchema, MessageType
from pyotp import random_base32, HOTP
from redis import Redis

from backend.config import EMAIl, PASSWORD, SERVER, REDIS_KEY, REDIS_HOST, REDIS_PORT
from backend.crud import manager, query_user
from backend.schemas import UserRegistrationRequest, VerifyUserOTP

conf = ConnectionConfig(
    MAIL_USERNAME=EMAIl,
    MAIL_PASSWORD=PASSWORD,
    MAIL_FROM=EMAIl,
    MAIL_PORT=465,
    MAIL_SERVER=SERVER,
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

router = APIRouter(prefix="/auth")
email_server = FastMail(conf)
redis_host = REDIS_HOST
redis_port = REDIS_PORT
redis_password = REDIS_KEY


@router.post("/login")
async def login(login_form: OAuth2PasswordRequestForm = Depends()):
    username = login_form.username
    password = login_form.password
    user = query_user(user=username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    elif checkpw(password.encode(), user.password.encode()):
        access_token = manager.create_access_token(data={"sub": username})
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"access_token": access_token, "token_type": "bearer"}
        )
    else:
        raise InvalidCredentialsException


@router.post("/register")
async def register(user: UserRegistrationRequest):
    global secret
    username = user.username
    email = user.email
    password = user.password
    user = query_user(user=username)
    if user is not None:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content="User already is already registered, please login"
        )
    else:
        redis_cache = Redis(host=redis_host, port=redis_port, password=redis_password, ssl=True)
        counter = redis_cache.lindex(email, -1)
        secret = redis_cache.lindex(email, 2)
        if counter is not None:
            counter = int(counter.decode()) + 1
            redis_cache.lset(email, -1, str(counter))
        else:
            counter = 0
            secret = random_base32()
            redis_cache.rpush(email, username, password, str(secret), str(counter))
            redis_cache.expire(email, 300)
        html = f"""
        <p>OTP: {HOTP(secret).at(counter)}</p>
        """
        message = MessageSchema(
            subject="Verify HealthCast Account",
            recipients=[email],
            body=html,
            subtype=MessageType.html
        )
        try:
            await email_server.send_message(message)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content="Verification email sent"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
        finally:
            redis_cache.connection_pool.close()


@router.post("/verify")
async def data(body: VerifyUserOTP):
    email = body.email
    otp = body.otp
    redis_cache = Redis(host=redis_host, port=redis_port, password=redis_password, ssl=True)
    username = redis_cache.lindex(email, 0)
    password = redis_cache.lindex(email, 1)
    secret = redis_cache.lindex(e