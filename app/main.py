from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_args_and_result = {}

    def inner(*args) -> Any:

        if args in stored_args_and_result:
            print("Getting from cache")

        else:
            print("Calculating new result")
            stored_args_and_result[args] = func(*args)
        return stored_args_and_result[args]
    return inner
