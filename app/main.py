from typing import Callable
from typing import Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key in cached_results:
            return cached_results[key]
        result = func(*args, **kwargs)
        cached_results[key] = result
        return result
    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)

