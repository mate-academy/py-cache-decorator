from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_res = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in stored_res:
            print("Getting from cache")
            return stored_res[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_res[key] = result
        return result
    return wrapper
