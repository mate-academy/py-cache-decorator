from typing import Callable, Any


def cache(func: Callable) -> Callable:
    caching = {}

    def wrapper(*args, **kwargs) -> Any:
        data = (args, frozenset(kwargs.items()))
        if data not in caching:
            print("Calculating new result")
            caching[data] = func(*args, **kwargs)
            return caching[data]
        print("Getting from cache")
        return caching[data]
    return wrapper
