from typing import Any, Callable
import functools


def cache(func: Callable) -> Callable:
    """Cache decorator that stores results for given arguments."""
    cached_results: dict[tuple[Any, ...], Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Wrapper that returns cached result if available."""
        key = (
            args,
            tuple(sorted(kwargs.items())),
        )

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[key] = result

        return result

    return wrapper
