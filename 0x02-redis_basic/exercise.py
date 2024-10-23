#!/usr/bin/env python3
"""
Cache class with Redis storage
"""

import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the count each time the method is called.
        """
        self._redis.incr(method.__qualname__)

        return method(self, *args, **kwargs)
    
    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The generated random key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, None]:
        """
        Retrieve data from Redis using the provided key. Optionally convert the data.

        Args:
            key (str): The key to retrieve the data.
            fn (Optional[Callable]): A callable used to convert the data.

        Returns:
            Union[str, bytes, int, None]: The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    
    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        Args:
            key (str): The key to retrieve the string data.

        Returns:
            Optional[str]: The retrieved string, or None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))


    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
            key (str): The key to retrieve the integer data.

        Returns:
            Optional[int]: The retrieved integer, or None if the key does not exist.
        """
        return self.get(key, int)