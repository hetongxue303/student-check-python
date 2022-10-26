"""
用户表
@Author:何同学
"""
from sqlalchemy import Column, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from base import Base


class User(Base):
    """用户表"""
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='用户ID')
    username = Column(String(100), nullable=False, index=True, comment='用户名')
    password = Column(String(200), nullable=False, server_default='123456', comment='用户密码')
