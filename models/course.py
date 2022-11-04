"""
课程表
@Author:何同学
"""
from sqlalchemy import BigInteger, Column, String, Integer

from models import Base


class Course(Base):
    """ 课程表 """
    __table_args__ = ({"comment": "课程表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='课程ID')

    name = Column(String(50), nullable=False, comment='课程名')

    detail = Column(String(200), nullable=False, server_default='该课程暂无描述！', comment='课程描述')

    # num = Column(Integer, nullable=False, server_default=0, comment='课程总人数')
