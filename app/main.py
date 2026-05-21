from typing import Callable, Any


def cache(func: Callable) -> Callable:
    func.cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in func.cache:
            print("Getting from cache")
            return func.cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func.cache[key] = result
            return result

    return wrapper
