from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Any:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]  # cache_dict - {(2, 3, 3): 2}
        else:
            function_result = func(*args)
            cache_dict[args] = function_result
            print("Calculating new result")
            return function_result

    return wrapper
