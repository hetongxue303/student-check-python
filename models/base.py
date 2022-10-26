"""
ORM父类
@Author:何同学
"""
from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    __name__: str  # 表名
    __table_args__ = {"mysql_charset": "utf8"}  # 设置表的字符集
    __mapper_args__ = {"eager_defaults": True}  # 防止 insert 插入后不刷新

    @declared_attr
    def __tablename__(cls) -> str:  # 将类名小写并转化为表名 __表名__
        return cls.__name__.lower()

    @declared_attr
    def create_time(cls):  # 创建时间
        return Column(DateTime(timezone=True), server_default=func.now(), comment='创建时间')

    @declared_attr
    def update_time(cls):  # 更新时间
        return Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment='更新时间')
