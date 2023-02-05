import functools
from typing import Callable
from typing import Union


def cache(func: Callable) -> int:
    cache_store = {}

    @functools.wraps(func)
    def inner(*args: Union[int, float, str, tuple]) -> \
            Union[int, float, str, tuple]:
        nonlocal cache_store
        if args in cache_store:
            print("Getting from cache")
        else:
            cache_store[args] = func(*args)
            print("Calculating new result")
        return cache_store[args]
    return inner
