"""
事件监听
@Author:何同学
"""
from fastapi import FastAPI
from api.apis import router
from core.config import settings
from database.mysql import init_db, drop_db, init_data
from exception.exception import init_exception


def init_project(app: FastAPI):
    @app.on_event('startup')
    async def startup():
        # 删除数据结果
        drop_db()
        # 初始化数据结构
        init_db()
        # 初始化表数据
        init_data()
        # 全局异常捕获注册
        init_exception(app)
        # 路由注册
        app.include_router(router, prefix=settings.API_PREFIX)
        print('启动成功 ---> 点击访问: http://127.0.0.1:8000/docs')

    @app.on_event('shutdown')
    async def shutdown():
        print('停止')
