from typing import Callable, Any


def cache(func: Callable) -> Callable:
    calculated = dict()

    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in calculated:
            print("Getting from cache")
            return calculated.get(key)
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            calculated[key] = result
            return result
    return inner
