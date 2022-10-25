from pydantic import BaseSettings


# 全局配置
class Settings(BaseSettings):
    APP_TITLE: str = '学生考勤系统'
    APP_BASE_API: str = '/api'
    APP_DEBUG: bool = True
    RELOAD = True

    LOG_PATH: str = 'tmp/app.log'

    JWT_SECRET_KEY: str = "ShsUP9qIP2Xui2GpXRY6y74v2JSVS0Q2YOXJ22VjwkI"
    JWT_EXPIRE: int = 24 * 60

    class Config:
        env_fil: str = '.env'
        case_sensitive: bool = True


settings = Settings()
