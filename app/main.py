from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    """Create an independent, persistent result cache for this function."""
    cached_results: dict[tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[key] = func(*args, **kwargs)
        return cached_results[key]

    return wrapper
