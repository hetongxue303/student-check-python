"""
中间件
@Author:何同学
"""
from fastapi import FastAPI, Request
from sqlalchemy.exc import OperationalError
from starlette.middleware.cors import CORSMiddleware

from core.config import settings
from schemas.result import fail

from core.logger import logger


def init_middleware(app: FastAPI):
    if settings.APP_CORS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_methods=['*'],
            allow_headers=['*'],
            allow_credentials=True
        )
        logger.info('跨域设置成功!!!')

    @app.middleware('http')
    async def intercept(request: Request, call_next):
        """ 拦截器 """
        logger.info(
            f"访问记录:IP:{request.client.host}-method:{request.method}-url:{request.url}--headers:{request.headers}")
        try:
            if request.headers.get('token'):
                return call_next(request)
        except OperationalError as e:
            logger.error(f'数据库连接失败 -- {e}')
            return fail(message='数据库连接失败')
