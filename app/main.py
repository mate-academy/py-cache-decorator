from functools import wraps
from typing import Callable, Any, Tuple


def _make_key(args: Tuple[Any, ...], kwargs: dict) -> Tuple[Any, ...]:

    if kwargs:

        kw_part = tuple(sorted(kwargs.items()))
    else:
        kw_part = ()
    return args + ("__KW__",) + kw_part


def cache(func: Callable) -> Callable:

    storage: dict[Tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = _make_key(args, kwargs)
        if key in storage:
            print("Getting from cache")
            return storage[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result

    return wrapper
