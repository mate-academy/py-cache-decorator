from typing import Callable, Any


def cache(func: Callable) -> Any:
    cache_data = {}

    def memory(*args: Callable) -> Any:
        if args in cache_data:
            print("Getting from cache")
            return cache_data[args]
        print("Calculating new result")
        func_result = func(*args)
        cache_data[args] = func_result
        return func_result

    return memory
