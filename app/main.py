from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> Any:
        print(
            "Getting from cache" if args in cached_results
            else "Calculating new result"
        )
        if args not in cached_results:
            cached_results[args] = func(*args)
        return cached_results[args]

    return wrapper
