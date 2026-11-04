from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key not in memory:
            print("Calculating new result")
            memory[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return memory[key]

    return wrapper
