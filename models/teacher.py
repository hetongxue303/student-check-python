"""
教师表
@Author:何同学
"""
from sqlalchemy import Column, String, BigInteger, Enum, Date, text

from models import Base


class Teacher(Base):
    """ 教师表 """
    __table_args__ = ({"comment": "教师表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='教师ID')

    no = Column(String(10), nullable=False, comment='教师工号')

    name = Column(String(100), nullable=False, comment='教师姓名')

    gender = Column(Enum('1', '2'), nullable=False, comment='教师性别')

    birthday = Column(Date(), nullable=False, comment='教师生日')

    address = Column(String(50), nullable=False, server_default=text("'重庆市渝北区'"), comment='地址')
