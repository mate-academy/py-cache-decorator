from functools import wraps
from typing import Any, Callable, Dict, Tuple


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cache:
            print("Getting from cache")
            return cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache[args] = result
            return result

    return wrapper
