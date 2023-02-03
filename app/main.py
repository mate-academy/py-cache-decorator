
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        arguments = (*args, *kwargs.values())

        if arguments not in results_dict:
            print("Calculating new result")
            results_dict[arguments] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return results_dict[arguments]
    return wrapper
