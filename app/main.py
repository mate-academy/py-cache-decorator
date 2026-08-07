from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_dict = {}

    def inner(*args: Any, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in results_dict:
            print("Getting from cache")
        else:
            results_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
        return results_dict[key]
    return inner
