from typing import Callable, Any


def cache(func: Callable) -> int:
    cache_result = {}

    def inner(*args: Any) -> Any:
        if args in cache_result:
            print("Getting from cache")
            return cache_result[args]
        print("Calculating new result")
        cache_result[args] = func(*args)
        return cache_result[args]
    return inner
