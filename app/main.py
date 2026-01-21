from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cache_ = {}

    def wrapper(*args, **kwargs) -> Any:
        arguments = (args, tuple(sorted(kwargs.items())))
        if arguments in cache_:
            print("Getting from cache")
            return cache_.get(arguments)
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_[arguments] = result

            return result

    return wrapper
