from typing import Callable

result_cache = {}


def cache(func: Callable) -> Callable:
    def new_result(*args, **kwargs) -> None:
        name_cache = func, args
        if name_cache in result_cache:
            print("Getting from cache")
            return result_cache[name_cache]

        else:
            result = func(*args, **kwargs)
            result_cache[name_cache] = result
            print("Calculating new result")
            return result
    return new_result
