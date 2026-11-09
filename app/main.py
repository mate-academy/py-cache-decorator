from functools import wraps
from typing import Callable


def _hashable(val):
    if isinstance(val, list):
        return (list, tuple(_hashable(x) for x in val))
    if isinstance(val, tuple):
        return (tuple, tuple(_hashable(x) for x in val))
    if isinstance(val, set):
        return (set, frozenset(_hashable(x) for x in val))
    if isinstance(val, dict):
        sorted_items = sorted(
            val.items(),
            key=lambda item: (str(type(item[0])), str(item[0]))
        )
        return (dict, tuple((k, _hashable(v)) for k, v in sorted_items))
    try:
        hash(val)
    except TypeError:
        raise TypeError(f"Unsupported unhashable type: {type(val)}")
    return (type(val), val)


def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (
            tuple(_hashable(a) for a in args),
            tuple(sorted(
                ((k, _hashable(v)) for k, v in kwargs.items()),
                key=lambda x: (str(type(x[0])), str(x[0]))
            ))
        )

        if key in memo:
            print("Getting from cache")
            return memo[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[key] = result
        return result

    return wrapper
