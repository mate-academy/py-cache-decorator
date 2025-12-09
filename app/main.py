from typing import Callable, Any, Dict, Tuple
from functools import wraps


def cache(func: Callable) -> Callable:
    # Storage must be initialized here to be captured by the wrapper function (closure).
    storage: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        # 1. Creating a single, hashable key for caching:

        # Sort kwargs items by key to ensure determinism (a=1, b=2 is the same as b=2, a=1)
        kwargs_tuple = tuple(sorted(kwargs.items()))

        # The complete key includes both positional arguments and sorted keyword arguments
        key = (args, kwargs_tuple)

        # 2. Caching logic
        if key in storage:
            print(f"Getting result from cache for key {key}")
            return storage[key]
        else:
            print(f"Calculating new result for key {key}")
            res = func(*args, **kwargs)
            storage[key] = res
            return res

    return wrapper

