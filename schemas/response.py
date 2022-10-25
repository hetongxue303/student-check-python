from typing import Any
from starlette import status
from starlette.responses import Response
from fastapi.responses import ORJSONResponse


# 成功返回
def success(code: int = 200, message: str = '请求成功', data: Any = None) -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': code,
            'message': message,
            'data': data
        }
    )


# 失败返回
def error(code: int = 400, message: str = '请求错误', data: Any = None) -> Response:
    return ORJSONResponse(
        status_code=code,
        content={
            'code': code,
            'message': message,
            'data': data
        }
    )
