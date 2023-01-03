from typing import Callable, Dict, Any


def cache(func: Callable) -> Callable:
    cache: Dict[Any, Any] = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in cache:
            print("Getting from cache")
            return cache[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[args] = result
            return result

    return wrapper
