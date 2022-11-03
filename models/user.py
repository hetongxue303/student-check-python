"""
用户表
@Author:何同学
"""
from sqlalchemy import Column, String, BigInteger, Enum

from models.base import Base


class User(Base):
    """用户表"""
    __table_args__ = ({"comment": "用户表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='用户ID')

    username = Column(String(100), nullable=False, comment='用户名')

    password = Column(String(200), nullable=False, comment='用户密码')

    type = Column(Enum('1', '2', '3'), nullable=False, server_default='3', comment='类型(1管理员 2教师 3学生)')

    last_login_ip = Column(String(50), nullable=False, comment='最后登录IP')
