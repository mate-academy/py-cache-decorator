from typing import Callable, Any, MutableSequence
from functools import wraps


def cache(func: Callable) -> Callable:
    _cache = {}

    @wraps(func)
    def wrapper(*args: not MutableSequence) -> Any:
        if args in _cache:
            print("Getting from cache")
            return _cache[args]

        func_result = func(*args)
        _cache[args] = func_result
        print("Calculating new result")
        return func_result

    return wrapper
