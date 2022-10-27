from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # 加密器


def verify_password(plain_password, hashed_password):  # 验证密码
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):  # 加密密码
    return pwd_context.hash(password)
