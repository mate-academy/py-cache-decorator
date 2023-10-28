from typing import Callable, Any
from functools import wraps


cached_func = {}


def cache(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (func, args, frozenset(kwargs.items()))
        if key in cached_func:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_func[key] = func(*args, **kwargs)
        return cached_func[key]
    return inner
