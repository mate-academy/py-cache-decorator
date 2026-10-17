from typing import Callable, Any
from functools import wraps


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    saved_results: dict[Any, Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in saved_results:
            print("Getting from cache")
            return saved_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        saved_results[key] = result
        return result

    return wrapper
