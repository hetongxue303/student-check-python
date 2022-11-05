"""
教师表
@Author:何同学
"""
from sqlalchemy import Column, String, BigInteger, Enum, Date, text, ForeignKey

from models import Base


class Teacher(Base):
    """ 教师表 """
    __table_args__ = ({"comment": "教师表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='教师ID')

    no = Column(String(10), nullable=False, comment='教师工号')

    name = Column(String(100), nullable=False, comment='教师姓名')

    gender = Column(Enum('1', '2'), server_default='1', nullable=False, comment='教师性别(1男2女)')

    birthday = Column(Date(), nullable=False, comment='教师生日')

    address = Column(String(50), nullable=False, server_default=text("'重庆市渝北区'"), comment='地址')

    major_id = Column(BigInteger, ForeignKey('major.id'), comment='专业ID')

    department_id = Column(BigInteger, ForeignKey('department.id'), comment='院系ID')
