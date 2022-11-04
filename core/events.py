"""
事件监听
@Author:何同学
"""
from fastapi import FastAPI


def init_event(app: FastAPI):
    @app.on_event('startup')
    async def startup():
        print('程序启动成功--->点击访问: http://127.0.0.1:8000/api/user/list')
        print('启动成功')

    @app.on_event('shutdown')
    async def shutdown():
        print('停止')
