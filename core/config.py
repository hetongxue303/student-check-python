"""
全局配置
@Author:何同学
"""
import secrets
from typing import List
from pydantic import BaseSettings, AnyHttpUrl

app_desc = """
    🎉 用户登录 🎉
    ✨ 账号: admin ✨
    ✨ 密码: 123456 ✨
"""


# 全局配置
class Settings(BaseSettings):
    """应用配置"""
    APP_TITLE: str = '学生考勤系统'  # 应用标题
    API_PREFIX: str = '/api'  # 接口前缀
    APP_DEBUG: bool = True  # 是否debug
    APP_CORS: bool = True  # 是否跨域
    APP_DESC: str = app_desc  # 描述
    APP_VERSION: str = '0.0.1'  # 版本
    STATIC_DIR: str = 'static'  # 静态文件目录
    GLOBAL_ENCODING: str = 'utf-8'  # 全局编码
    CORS_ORIGINS: List[AnyHttpUrl] = ['http://127.0.0.1:3000', 'http://127.0.0.1:5179']  # 跨域请求(列表)
    RELOAD: bool = True  # 热部署

    """数据源配置"""
    REDIS_URI: str = 'redis://:123456@127.0.0.1:6379/1'  # redis
    DATABASE_URI: str = 'mysql+pymysql://root:123456@127.0.0.1:3306/student_check?charset=utf8'  # mysql
    DATABASE_ECHO: bool = False  # 是否打印数据库日志 (可看到创建表、表数据增删改查的信息)

    """JWT配置"""
    JWT_SECRET_KEY: str = secrets.token_urlsafe(32)  # 密钥(每次重启服务密钥都会改变, token解密失败导致过期, 可设置为常量)
    JWT_EXPIRE: int = 24 * 60 * 1  # token过期时间: 60 minutes * 24 hours * 1 days = 1 days

    class Config:
        env_fil: str = '.env'
        case_sensitive: bool = True  # 区分大小写


settings = Settings()
