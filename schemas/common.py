from datetime import datetime
from pydantic import BaseModel, validator


class GMT(BaseModel):  # 时间字段处理
    create_time: datetime
    update_time: datetime

    @validator("create_time", "update_time")
    def format_time(cls, value: datetime) -> str:
        return value.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间
