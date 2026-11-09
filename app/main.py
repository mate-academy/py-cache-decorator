from functools import wraps
from typing import Callable, Any


def make_hashable(val: Any) -> Any:
    if isinstance(val, (list, tuple)):
        return tuple(make_hashable(x) for x in val)
    if isinstance(val, set):
        return frozenset(make_hashable(x) for x in val)
    if isinstance(val, dict):
        return tuple(sorted((str(k), make_hashable(v)) for k, v in val.items()))
    return val


def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (make_hashable(args), make_hashable(kwargs))

        if key in memo:
            print("Getting from cache")
            return memo[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[key] = result
        return result

    return wrapper
    return wrapper
