from typing import Callable, Any


def cache(func: Callable) -> Callable:
    inputs = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in inputs:
            print("Getting from cache")
            return inputs[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        inputs[key] = result
        return result
    return wrapper
