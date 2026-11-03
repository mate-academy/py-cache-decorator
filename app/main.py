
from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key not in results:
            results[key] = func(*args, **kwargs)

        return results[key]

    return wrapper
