"""
mysql会话
@Author:何同学
"""
from asyncio import current_task
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import sessionmaker

from core.config import settings
from models.base import Base

# 创建表引擎
engine = create_async_engine(
    url=settings.DATABASE_URI,
    echo=settings.DATABASE_ECHO,
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池中数量的大小
    pool_timeout=30,  # 连接池中没有连接的时候的最长的等待秒数，超时则报错
    pool_recycle=-1  # 默认值是 -1，不回收,多久之后对线程池中的线程进行一次连接的回收
)

# 操作表会话
async_session_factory = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False  # 防止提交后属性过期
)

async_session = async_scoped_session(async_session_factory, scopefunc=current_task)


def init_db():  # 创建所有表
    Base.metadata.create_all(engine)


def drop_db():  # 删除表的所有函数。执行
    Base.metadata.drop_all(engine)
