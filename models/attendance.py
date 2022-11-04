"""
考勤表
@Author:何同学
"""
from sqlalchemy import BigInteger, Column, String, Integer, Enum, DateTime

from models import Base


class Attendance(Base):
    """ 考勤表 """
    __table_args__ = ({"comment": "考勤表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='考勤ID')

    status = Column(Enum('0', '1'), nullable=False, server_default='0', comment='状态(0未考勤 1已考勤)')
