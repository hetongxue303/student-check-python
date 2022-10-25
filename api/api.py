from fastapi import APIRouter
from api.system import user

router = APIRouter()

# system模块
router.include_router(user.router, prefix='/system', tags=['system'])
