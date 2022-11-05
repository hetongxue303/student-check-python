"""
管理员表
@Author:何同学
"""
from sqlalchemy import Column, String, BigInteger, Enum, Date, text

from models import Base


class Admin(Base):
    """ 管理员表 """
    __table_args__ = ({"comment": "管理员表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='管理员ID')

    name = Column(String(200), nullable=False, comment='管理员名称')

    gender = Column(Enum('1', '2'), server_default='1', nullable=False, comment='性别(1男2女)')

    birthday = Column(Date(), nullable=False, comment='生日')

    address = Column(String(50), nullable=False, server_default=text("'重庆市渝北区'"), comment='地址')
