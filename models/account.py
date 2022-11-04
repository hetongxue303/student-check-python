"""
账户表
@Author:何同学
"""
from sqlalchemy import Column, String, BigInteger, DateTime, func

from models import Base


class Account(Base):
    """ 账户表 """
    __table_args__ = ({"comment": "账户表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='账户ID')

    username = Column(String(100), nullable=False, comment='用户名')

    password = Column(String(200), nullable=False, comment='用户密码')

    last_login_time = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), comment='最后登录时间')

    last_login_ip = Column(String(50), nullable=False, comment='最后登录IP')
