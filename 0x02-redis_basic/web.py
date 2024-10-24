#!/usr/bin/env python3
"""
Web cache and URL access tracker with Redis
"""

import requests
import redis
from typing import Callable
from functools import wraps

redis_instance = redis.Redis()


def cache_page(method: Callable) -> Callable:
    """
    Decorator to cache the content of the page and track access count.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        redis_instance.incr(f"count:{url}")

        cached_page = redis_instance.get(f"cached:{url}")
        if cached_page:
            print("Cache hit")
            return cached_page.decode('utf-8')

        print("Cache miss, fetching page content...")
        page_content = method(url)

        redis_instance.setex(f"cached:{url}", 10, page_content)

        return page_content
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a given URL.
    If the content is already cached, return it from cache.
    """
    response = requests.get(url)
    return response.text
