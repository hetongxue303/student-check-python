from fastapi import FastAPI
from core.config import settings
from starlette.middleware.cors import CORSMiddleware
from api.api import router

# 实例化 app
app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESC,
    openapi_url=f'{settings.API_PREFIX}/openapi.json',
    version=settings.APP_VERSION,
    debug=settings.APP_DEBUG
)

# 配置跨域 cors
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
