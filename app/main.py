from typing import Callable

cache_list = {}


def cache(func: Callable) -> Callable:
    def wrapper(*args) -> int:
        cache_list.setdefault(func, {})

        if args in cache_list[func]:
            print("Getting from cache")
            return cache_list[func][args]

        print("Calculating new result")
        result = func(*args)
        cache_list[func][args] = result
        return result

    return wrapper
