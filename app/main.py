from typing import Callable
import functools

_function_caches = {}
def cache(func: Callable) -> Callable:
    if func not in _function_caches:
        _function_caches[func] = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sorted_kwargs = tuple(sorted(kwargs.items()))
        cache_key = (args, sorted_kwargs)
        if cache_key in _function_caches[func]:
            print("Getting from cache")
            return _function_caches[func][cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            _function_caches[func][cache_key] = result
        return result
    return wrapper
