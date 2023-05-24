from typing import Any


def cache(func: callable) -> callable:
    cache_vault = {}

    def inner(*args) -> Any:
        if args not in cache_vault:            
            print("Calculating new result")
            cache_vault[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_vault[args]
    return inner
