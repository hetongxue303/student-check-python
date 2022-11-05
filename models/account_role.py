"""
账户角色表
@Author:何同学
"""
from sqlalchemy import BigInteger, Column, ForeignKey

from models import Base


class Account_Role(Base):
    """ 账户角色信息表 """
    __table_args__ = ({"comment": "账户角色表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True, comment='主键ID')

    account_id = Column(BigInteger, ForeignKey('account.id'), comment='账户ID')

    role_id = Column(BigInteger, ForeignKey('role.id'), comment='账户ID')
