"""
学生表
@Author:何同学
"""
from models import Base

from sqlalchemy import Column, BigInteger, String, Date, Enum, text


class Student(Base):
    """学生表"""
    __table_args__ = ({"comment": "学生表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='学生ID(学号)')

    name = Column(String(200), nullable=False, comment='学生姓名')

    gender = Column(Enum('1', '2'), nullable=False, comment='性别')

    birthday = Column(Date(), nullable=False, comment='生日')

    address = Column(String(50), nullable=False, server_default=text("'重庆市渝北区'"), comment='地址')
