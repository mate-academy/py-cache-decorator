from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        call_signature = (args, tuple(sorted(kwargs.items())))
        if call_signature in results_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results_cache[call_signature] = func(*args, **kwargs)
        return results_cache[call_signature]

    return wrapper
