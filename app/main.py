from typing import Callable


def cache(func: Callable) -> Callable:
    cached = dict()

    def wrapper(*args, **kwargs) -> int:
        cache_tuple = (*args, frozenset(kwargs.items()))

        cached_result = cached.get(cache_tuple)
        if cached_result is not None:
            print("Getting from cache")
            return cached_result

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached[cache_tuple] = result
        return result

    return wrapper
