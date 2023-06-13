from typing import Callable, Any


def cache(func: Callable) -> Callable:

    store = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.values())
        if key in store:
            print("Getting from cache")
            return store[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        store[key] = result
        return result

    return wrapper
