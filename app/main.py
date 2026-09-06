import functools
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    """
    Cache results of `func` for functions that take only immutable
    (hashable) arguments.

    Each function decorated with `cache` gets its own isolated storage
    (created fresh in this closure every time `cache` is applied), so
    several decorated functions used at the same time never share
    or overwrite each other's cached results.
    """
    stored_results = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_results[key] = result
        return result

    return wrapper
