from typing import Callable, Any
result_cache = {}


def cache(func: Callable) -> Any:
    def new_result(*args, **kwargs) -> Any:
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
