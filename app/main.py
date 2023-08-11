from typing import Callable


def cache(func: Callable) -> Callable:
    cached = dict()

    def wrapper(*args, **kwargs) -> int:
        cache_tuple = (*args, frozenset(kwargs.items()))
        for cached_args, cached_result in cached.items():
            if cached_args == cache_tuple:
                print("Getting from cache")
                return cached_result

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached[cache_tuple] = result
        return result

    return wrapper
