from typing import Any


def cache(func: callable) -> callable:
    cache_vault = {}

    def inner(*args) -> Any:
        if args in cache_vault:
            print("Getting from cache")
            return cache_vault[args]
        print("Calculating new result")
        result = func(*args)
        cache_vault[args] = result
        return result
    return inner
