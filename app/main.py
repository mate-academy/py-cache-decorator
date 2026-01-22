from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_list = []

    def inner(*args, **kwargs) -> Any:
        kwargs_tuple = tuple(sorted(kwargs.items()))
        cache_key = (args, kwargs_tuple)

        for cached_key, result in cache_list:
            if cached_key == cache_key:
                print("Getting from cache")
                return result

        function_result = func(*args, **kwargs)
        cache_list.append((cache_key, function_result))
        print("Calculating new result")
        return function_result

    return inner
