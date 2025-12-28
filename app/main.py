from typing import Any, Callable
from functools import wraps
from inspect import signature

def cache(func: Callable) -> Callable:
    store = {}
    sig = signature(func)

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Canonicalize arguments → match them to parameter names
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        # Convert bound arguments to a hashable key
        key = tuple(bound.arguments.items())

        if key in store:
            print("Getting from cache")
            return store[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        store[key] = result
        return result

    return wrapper
