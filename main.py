"""
程序入口类
@Author:何同学
"""

from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from core.config import settings
from api.router import router
from core.plugin.exceptions import init_exception

# 实例化 fastapi
app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESC,
    openapi_url=f'{settings.API_PREFIX}/openapi.json',
    version=settings.APP_VERSION,
    debug=settings.APP_DEBUG
)

# 局异常捕获全注册 exceptions
# init_exception(app)

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
