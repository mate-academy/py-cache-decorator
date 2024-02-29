from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(*args: list) -> list:
        old_cach = args
        list_of_old_cache = []
        if old_cach not in list_of_old_cache:
            list_of_old_cache.append(old_cach)
            return "Calculating new result"
        return "Getting from cache"
    return inner
