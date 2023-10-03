from typing import Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        if not hasattr(wrapper, "cache_results"):
            wrapper.cache_results = {}
        arg_key = (args, frozenset(kwargs.items()))
        if arg_key in wrapper.cache_results:
            print("Getting from cache")
            result = wrapper.cache_results[arg_key]
        else:
            print("Calculating and caching result")
            result = func(*args, **kwargs)
            wrapper.cache_results[arg_key] = result
        return result

    return wrapper
