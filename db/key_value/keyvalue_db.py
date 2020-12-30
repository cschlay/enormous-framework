"""
The current key-value database in use is Redis.
"""
import os
from typing import Optional

import redis as redis


def get_connection(auto_decode: bool = True) -> redis.Redis:
    """
    Returns a redis connection.
    """
    return redis.Redis(
        host=os.environ["REDIS_HOST"],
        port=os.environ["REDIS_PORT"],
        db=os.environ["REDIS_DB"],
        decode_responses=auto_decode,
    )


def get(key: str) -> Optional[any]:
    """
    Get value proxy function for redis storage.
    :param key: to lookup value from.
    :return: the value stored if exists
    """
    raise NotImplemented


def set(key: str, value: any):
    """
    Set value proxy function for redis storage.

    :param key:
    :param value:
    """
    connection: redis.Redis = get_connection()
    connection.set(key, str(value))
