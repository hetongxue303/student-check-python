from schemas.response import success, fail
from fastapi import APIRouter

router = APIRouter()


@router.get('/list')
async def get_user():
    return success()


@router.get('/list1')
async def get_user():
    return fail()
