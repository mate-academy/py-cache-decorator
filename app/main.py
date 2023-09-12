from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_long_function = dict()

    def inner(*args, **kwargs) -> Any:
        args_key = args
        kwargs_key = frozenset(kwargs.items())

        if (args_key, kwargs_key) not in results_long_function:
            print("Calculating new result")
            results_long_function[args_key, kwargs_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return results_long_function[args_key, kwargs_key]
    return inner
