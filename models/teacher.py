"""
教师表
@Author:何同学
"""
from sqlalchemy import Column, String, BigInteger

from models.base import Base


class Teacher(Base):
    """用户表"""
    __table_args__ = ({"comment": "教师表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='教师ID')

    username = Column(String(100), nullable=False, comment='用户名')

    password = Column(String(200), nullable=False, comment='用户密码')

    last_login_ip = Column(String(50), nullable=False, comment='最后登录IP')
