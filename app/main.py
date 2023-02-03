from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_hash_result = {}

    @wraps(func)
    def results_save_wrapper(*args, **kwargs) -> None:
        func_arg_kwarg_hash = hash(args) + hash(func)

        for item in kwargs.items():
            func_arg_kwarg_hash += hash(item)

        if cache_hash_result.get(func_arg_kwarg_hash) is not None:
            print("Getting from cache")
            return cache_hash_result.get(func_arg_kwarg_hash)

        print("Calculating new result")
        cache_hash_result[func_arg_kwarg_hash] = func(*args, **kwargs)
        return cache_hash_result.get(func_arg_kwarg_hash)

    return results_save_wrapper
