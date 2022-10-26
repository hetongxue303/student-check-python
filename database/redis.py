"""
redis配置
@Author:何同学
"""
import json

from aioredis import Redis
from core.config import settings


class redis(Redis):

    async def list_loads(self, key: str, num: int = -1) -> list:  # 将列表字符串转为对象
        todo_list = await self.lrange(key, 0, (num - 1) if num > -1 else num)
        return [json.loads(todo) for todo in todo_list]

    async def cus_lpush(self, key: str, value: str | list | dict):  # 向列表右侧插入数据
        text = json.dumps(value)
        await self.lpush(key, text)

    async def get_list_by_index(self, key: str, id: int) -> object:  # 根据索引得到列表值
        value = await self.lindex(key, id)
        return json.loads(value)


async def init_redis() -> redis:  # 连接redis
    return await redis.from_url(url=settings.REDIS_URI,
                                encoding=settings.GLOBAL_ENCODING,
                                decode_responses=True)
