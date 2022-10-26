from schemas.result import success, fail
from fastapi import APIRouter

from schemas import login

router = APIRouter()


@router.get('/list', response_model=login.Login, summary='列表接口')
async def get_user():
    return success()


@router.get('/list1')
async def get_user():
    return fail()
