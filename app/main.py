from typing import Callable, Any


def cache(func: Callable) -> Callable:
    chache_dict = {}

    def inner(*args) -> Any:
        if args not in chache_dict:
            print("Calculating new result")
            function_result = func(*args)
            chache_dict[args] = function_result
            return function_result

        print("Getting from cache")
        return chache_dict[args]

    return inner
