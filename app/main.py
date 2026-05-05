from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached_results: dict[tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]

        print("Calculating new result")
        result = func(*args)
        cached_results[args] = result
        return result

    return wrapper
