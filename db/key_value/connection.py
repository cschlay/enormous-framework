"""
The current key-value database in use is Redis.
"""
import os

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
