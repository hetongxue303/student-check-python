"""
专业表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String

from models import Base


class Major(Base):
    """ 专业表 """
    __table_args__ = ({"comment": "专业表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='专业ID')

    name = Column(String(50), nullable=False, comment='专业名称')
