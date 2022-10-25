from timeit import timeit

from fastapi import APIRouter

router = APIRouter()


@router.get('/list')
async def get_user():
    return 'hello system'
