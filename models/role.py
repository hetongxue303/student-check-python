"""
角色表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String

from models import Base


class Role(Base):
    """ 角色表 """
    __table_args__ = ({"comment": "角色表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='角色ID')

    name = Column(String(50), nullable=False, comment='角色名字')

    key = Column(String(50), nullable=False, comment='角色key')
