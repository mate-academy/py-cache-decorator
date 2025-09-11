from typing import Callable, Any


def cache(func: Callable) -> Any:
    storage = {}

    def inner(*args: float | int | str | bool | tuple) -> Any:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            func_result = func(*args)
            storage[args] = func_result
            return func_result
    return inner
