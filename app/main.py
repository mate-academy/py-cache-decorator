from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_element = ""
        for arg in args:
            cache_element += str(arg)

        for kwarg in kwargs:
            cache_element += str(kwarg)

        if cache_element not in cache_dict:
            cache_dict[cache_element] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_dict[cache_element]

    return wrapper
