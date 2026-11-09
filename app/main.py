from functools import wraps
from typing import Callable, Any


def _hashable(val: Any) -> Any:
    if isinstance(val, list):
        return tuple(_hashable(x) for x in val)
    if isinstance(val, dict):
        return tuple(sorted((k, _hashable(v)) for k, v in val.items()))
    if isinstance(val, set):
        return frozenset(_hashable(x) for x in val)
    return val


def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (
            tuple(_hashable(a) for a in args),
            tuple(sorted((k, _hashable(v)) for k, v in kwargs.items()))
        )

        if key in memo:
            print("Getting from cache")
            return memo[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[key] = result
        return result

    return wrapper
