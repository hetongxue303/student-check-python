"""
路由配置类
@Author:何同学
"""
from fastapi import APIRouter
from api.system import user

router = APIRouter()

# system模块
router.include_router(user.router, prefix='/system', tags=['系统模块'])
