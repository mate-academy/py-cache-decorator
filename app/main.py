from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results: dict[Any, Any] = {}

    @wraps(func)
    def inner(*args: Any) -> Any:
        if args in cached_results:
            print("Getting from cache")

            return cached_results[args]
        else:
            print("Calculating new result")

            result = func(*args)

            cached_results[args] = result

            return result

    return inner
