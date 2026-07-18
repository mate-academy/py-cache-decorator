import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if args in cache_data:
            print("Getting from cache")
            return cache_data [args]

        print("Calculating new result")
        result = func(*args, **kwargs)

        cache_data[args] = result
        return result

    return wrapper


@cache
def add(first_number: int, second_number: int) -> int:
    return first_number + second_number