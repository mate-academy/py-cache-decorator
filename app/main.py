from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_values = {}

    def wrapper(*args) -> Any:
        if args in cached_values.keys():
            print("Getting from cache")
            return cached_values[args]
        print("Calculating new result")
        function_result = func(*args)
        cached_values[args] = function_result
        return function_result

    return wrapper
