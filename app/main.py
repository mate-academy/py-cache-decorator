from typing import Callable, Any


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        key_cache = (args, tuple(sorted(kwargs.items())))
        if key_cache in wrapper.cache:
            print("Getting from cache")
            return wrapper.cache[key_cache]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            wrapper.cache[key_cache] = result
            return result
    wrapper.cache = {}
    return wrapper
