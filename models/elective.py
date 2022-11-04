"""
选修表
@Author:何同学
"""
import decimal

from sqlalchemy import Column, BigInteger, String, Date, Enum, text, DECIMAL

from models import Base


class Elective(Base):
    """ 选修表 """
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='选修ID')

    score = Column(DECIMAL(3, 2), nullable=True, comment='成绩')
