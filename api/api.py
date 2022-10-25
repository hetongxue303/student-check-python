from fastapi import APIRouter
from .user import user

router = APIRouter()

# 引入路由
router.include_router(router=user.router, prefix='/user', tags=['user'])
