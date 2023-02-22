from typing import Any


def cache(func: callable) -> callable:
    data_cache = {}

    def inner(*args) -> Any:
        if args in data_cache:
            print("Getting from cache")
            return data_cache[args]
        else:
            result = func(*args)
            data_cache[args] = result
            print("Calculating new result")
            return result

    return inner
