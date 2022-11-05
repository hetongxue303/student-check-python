"""
教师课程表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, ForeignKey

from models import Base


class Teacher_Course(Base):
    """ 教师课程表 """
    __table_args__ = ({"comment": "教师课程表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='主键ID')

    teacher_id = Column(BigInteger, ForeignKey('teacher.id'), comment='教师ID')

    course_id = Column(BigInteger, ForeignKey('course.id'), comment='课程ID')
