from typing import Callable
from functools import wraps
from typing import Any, Dict, Tuple


def cache(func: Callable) -> Callable:
    cache_store: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_store[key] = result
            return result

    return wrapper
