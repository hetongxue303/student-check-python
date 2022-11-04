from datetime import timedelta, datetime
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status
from models.account import User
from database.mysql import get_db
from schemas.token import TokenData

SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM: str = "HS256"

oauth2 = OAuth2PasswordBearer(tokenUrl="/login")
crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")  # 实例化加密器


def get_user(username: str, db: Session = Depends(get_db())) -> User:  # 获取用户信息
    return db.query(User).filter(User.username == username).first()


def authenticate_user(username: str, password: str) -> User | bool:  # 认证用户
    user: User = get_user(username)
    if not user:  # 是否存在用户
        return False
    if not verify_password(password, user.password):  # 校验密码
        return False
    return user


def get_current_user(token: str = Depends(oauth2)):  # 获取当前登录用户
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def create_token(data: dict, expires_time: timedelta | None = None):  # 生成token
    to_encode = data.copy()
    if expires_time:
        expire = datetime.utcnow() + expires_time
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def verify_password(plain_password, hashed_password) -> bool:  # 验证密码
    return crypt.verify(plain_password, hashed_password)


async def encryption_password(password: str) -> str:  # 加密密码
    return crypt.hash(password)
