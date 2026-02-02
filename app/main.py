from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_results = {}

    def inner(*args, **kwargs) -> Any:
        argumets = (args, tuple(kwargs.values()))

        if argumets in cache_results:
            print("Getting from cache")
            return cache_results[argumets]

        result = func(*args, **kwargs)
        cache_results[argumets] = result
        print("Calculating new result")
        return result
    return inner
