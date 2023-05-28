from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_values = {}

    def wrapper(*args) -> Any:
        func_name = func.__name__
        if func_name not in cached_values.keys():
            cached_values[func_name] = {}
        if args in cached_values[func_name].keys():
            print("Getting from cache")
            return cached_values[func_name][args]
        print("Calculating new result")
        function_result = func(*args)
        cached_values[func_name][args] = function_result
        return function_result

    return wrapper
