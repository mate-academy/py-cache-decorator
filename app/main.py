from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_args_and_result = {}

    def inner(*args) -> Any:

        if args in stored_args_and_result:
            print("Getting from cache")
            return stored_args_and_result[args]
        else:
            result = func(*args)
            print("Calculating new result")
            stored_args_and_result[args] = result
            return result

    return inner
