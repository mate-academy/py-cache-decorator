from typing import Callable, Any


def cache(func: Callable) -> Callable:

    storage = {}

    def inner(*args: Any, **kwargs: Any) -> Callable:
        if args and args in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args, **kwargs)
        return storage.get(args)

    return inner
