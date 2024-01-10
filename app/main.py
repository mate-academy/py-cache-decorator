from typing import Callable, Any


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())

        if key not in wrapper.results:
            value_result = func(*args, **kwargs)
            wrapper.results[key] = value_result
            print("Calculating new result")

        else:
            print("Getting from cache")

        return wrapper.results[key]

    wrapper.results = {}
    return wrapper
