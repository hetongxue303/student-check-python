"""
程序入口
@Author:何同学
"""

from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from core.config import settings
from core.events import init_project

# 实例化 fastapi
app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESC,
    openapi_url=f'{settings.API_PREFIX}/openapi.json',
    version=settings.APP_VERSION,
    debug=settings.APP_DEBUG
)

# 事件监听注册
init_project(app)
