"""
事件监听
@Author:何同学
"""
from fastapi import FastAPI


def init_event(app: FastAPI):
    @app.on_event('startup')
    async def startup():
        print('程序启动成功...通过: http://127.0.0.1:8000/api/user/list 访问')

    @app.on_event('shutdown')
    async def shutdown():
        print('程序已停止...')
