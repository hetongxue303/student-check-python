"""
路由配置
@Author:何同学
"""
from fastapi import APIRouter
from api.system import user
from api.login import login

router = APIRouter()

# system模块
router.include_router(user.router, prefix='/user', tags=['系统模块'])
