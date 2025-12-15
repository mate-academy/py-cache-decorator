from functools import wraps
from typing import Callable, Any


def is_inmutable(value: Any) -> bool:
    return isinstance(value, (int, float, complex, str,
                              tuple, frozenset, bytes))
    """Check if argument is inmutable."""


def cache(func: Callable) -> Callable:
    store = {}  # Contains cached results

    @wraps(func)
    def inner(*args, **kwargs) -> Any:

        arg = all(is_inmutable(value)for value in args)
        kwarg = all(is_inmutable(value)
                    for value in tuple(sorted(kwargs.items())))

        if not (arg and kwarg):
            return func(*args, **kwargs)

        key = (args, frozenset(kwargs.items()))

        if key in store:
            print("Getting from cache")
            return store.get(key)
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            store[key] = result
            return result
    return inner
