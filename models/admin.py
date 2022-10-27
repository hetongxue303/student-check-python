"""
用户表
@Author:何同学
"""
from sqlalchemy import Column, String, BigInteger, DateTime, func

from database.mysql import Base


class User(Base):
    """用户表"""
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='用户ID')
    username = Column(String(100), nullable=False, index=True, comment='用户名')
    password = Column(String(200), nullable=False, comment='用户密码')
    create_time = Column(DateTime(timezone=True), server_default=func.now(), comment='创建时间')
    update_time = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment='更新时间')
