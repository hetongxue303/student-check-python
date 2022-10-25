from fastapi import FastAPI
from base.config import settings
from starlette.middleware.cors import CORSMiddleware
from api import router

# 实例化fastapi
app = FastAPI(
    title=settings.APP_TITLE,
    description='学生考勤系统 文档',
    openapi_url=f"{settings.APP_BASE_API}/openapi.json",
    version='0.0.1',
    debug=settings.APP_DEBUG)

# 配置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True
)

# 配置路由
app.include_router(router, prefix=settings.APP_BASE_API)
