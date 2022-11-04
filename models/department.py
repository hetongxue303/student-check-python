"""
院系表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship

from models import Base


class Department(Base):
    """ 院系表 """
    __table_args__ = ({"comment": "院系表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='学院ID')

    name = Column(String(50), nullable=False, comment='学院名称')
