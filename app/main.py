from functools import wraps
from typing import Callable, Any, Tuple


def cache(func: Callable) -> Callable:
    memory = {}

    @wraps(func)
    def wrapper(*args: Tuple[Any], **kwargs: Any) -> Any:
        key = (func, args, frozenset(kwargs.items()))
        if key in memory:
            print("Getting from cache")
            return memory[key]
        else:
            print("Calculating new result")
            memory[key] = func(*args, **kwargs)
            return memory[key]

    return wrapper
