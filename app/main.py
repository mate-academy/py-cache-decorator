from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_results: dict[
        tuple[tuple[Any, ...], tuple[tuple[str, Any], ...]], Any
    ] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in stored_results:
            print("Getting from cache")
            return stored_results[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_results[cache_key] = result
        return result

    return wrapper
