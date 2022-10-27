"""
程序入口
@Author:何同学
"""

from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from core.config import settings
from api.apis import router
from core.events import init_event
from exception.exception import init_exception
from database.mysql import init_db

# 实例化 fastapi
app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESC,
    openapi_url=f'{settings.API_PREFIX}/openapi.json',
    version=settings.APP_VERSION,
    debug=settings.APP_DEBUG
)

# 事件监听注册 event
init_event(app)

# 全局异常捕获注册 exception
init_exception(app)

# 初始化表结构
init_db()

# 跨域注册 cors
if settings.APP_CORS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
        allow_credentials=True
    )

# 路由注册 router
app.include_router(router, prefix=settings.API_PREFIX)
