from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args) -> Any:
        nonlocal cache_data
        name = func.__name__

        if name in cache_data:
            if args in cache_data[name]:
                print("Getting from cache")
                return cache_data[name][args]
            result = func(*args)
            cache_data[name][args] = result
            print("Calculating new result")
            return result
        result = func(*args)
        cache_data[name] = {args: result}
        print("Calculating new result")
        return result
    return wrapper
