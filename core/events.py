"""
事件监听
@Author:何同学
"""
from fastapi import FastAPI

from database.redis import init_redis


def init_event(app: FastAPI):
    @app.on_event('startup')
    async def startup():
        print('程序启动成功--->点击访问: http://127.0.0.1:8000/api/user/list')
        app.state.redis = await init_redis()  # 初始化redis
        print(f'redis连接成功:{app.state.redis}')

    @app.on_event('shutdown')
    async def shutdown():
        app.state.resis.close()
        await app.state.redis.wait_closed()
