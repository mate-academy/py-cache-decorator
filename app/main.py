from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    store: dict[str, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key: str = f"{func.__name__}_{str(args)}_{str(kwargs)}"
        if key not in store:
            print("Calculating new result")
            store[key] = func(*args,**kwargs)
        else:
            print("Getting from cache")

        return store[key]

    return wrapper
