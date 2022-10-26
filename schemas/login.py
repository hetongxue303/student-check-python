from pydantic import BaseModel


class Login(BaseModel):  # 登陆模型
    username: str
    password: str
