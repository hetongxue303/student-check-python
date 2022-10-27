from schemas.result import success, fail
from fastapi import APIRouter

router = APIRouter()


@router.get('/list', summary='列表接口')
async def get_user():
    return success()


@router.get('/list1')
async def get_user():
    return fail()
