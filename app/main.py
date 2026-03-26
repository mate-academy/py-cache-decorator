import functools
from typing import Callable


def make_hashable(value):
    if isinstance(value, list):
        return tuple(make_hashable(x) for x in value)
    if isinstance(value, dict):
        return tuple(sorted((k, make_hashable(v)) for k, v in value.items()))
    if isinstance(value, (set, frozenset)):
        return tuple(sorted(make_hashable(x) for x in value))
    return value


def cache(func: Callable) -> Callable:
    stored_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            hashable_args = tuple(make_hashable(a) for a in args)
            hashable_kwargs = tuple(sorted((k, make_hashable(v)) for k, v in kwargs.items()))
            key = (hashable_args, hashable_kwargs)
        except TypeError:
            raise TypeError("cache decorator supports only immutable and hashable arguments")

        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_results[key] = result
        return result

    wrapper.cache = stored_results
    return wrapper