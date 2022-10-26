"""
日志配置
@Author:何同学
"""
import os
from loguru import logger
from utils.file_utils import create_dir
from typing import List

from core.config import settings


# 创建日志文件名
def logger_file() -> str:
    # 创建日志文件名
    log_path: str = create_dir(settings.LOGGER_DIR)

    # 创建文件列表
    file_list: List[str] = os.listdir(log_path)
    if len(file_list) > 3:
        os.remove(os.path.join(log_path, file_list[0]))

    # 日志输出路径
    return os.path.join(log_path, settings.LOGGER_NAME)


logger.add(
    logger_file(),
    encoding=settings.GLOBAL_ENCODING,
    level=settings.LOGGER_LEVEL,
    rotation=settings.LOGGER_ROTATION,
    retention=settings.LOGGER_RETENTION,
    enqueue=True
)
