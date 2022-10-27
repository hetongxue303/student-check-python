"""
mysql会话
@Author:何同学
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings

# 创建引擎
engine = create_engine(
    url=settings.DATABASE_URI,  # MySQL URI
    echo=settings.DATABASE_ECHO,  # 是否打印数据库日志 (可看到创建表、表数据增删改查的信息)
)

# 操作数据库会话
localSession = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False  # 防止提交后属性过期
)

# 基类表
Base = declarative_base()


def init_db():  # 创建表结构
    Base.metadata.create_all(engine)


def drop_db():  # 删除表的所有函数
    Base.metadata.drop_all(engine)


def get_db():  # 获取数据库
    try:
        db = localSession()
        yield db
    finally:
        db.close()
