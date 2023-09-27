from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> Any:
        result = (
            cached_results[args] if args in cached_results
            else func(*args)
        )
        print(
            "Getting from cache" if args in cached_results
            else "Calculating new result"
        )
        cached_results[args] = result
        return result

    return wrapper
