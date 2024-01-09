from typing import Callable


def cache(func: Callable) -> Callable:
    cached_result = {}

    def wrapper(*args, **kwargs) -> str:
        cache_key = func(args, tuple(sorted(kwargs.items())))
        if cache_key in cached_result:
            print("Getting from cache")
            return cached_result[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_result[cache_key] = result
            return result
    return wrapper


@cache
def pass_through_function(*args, **kwargs) -> tuple:
    return args, kwargs
