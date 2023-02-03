from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_hash_result = {}

    @wraps(func)
    def results_save_wrapper(*args, **kwargs) -> Any:
        func_arg_kwarg_hash = (*args, *kwargs.items(), hash(func))

        if cache_hash_result.get(func_arg_kwarg_hash) is not None:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_hash_result[func_arg_kwarg_hash] = func(*args, **kwargs)

        return cache_hash_result.get(func_arg_kwarg_hash)

    return results_save_wrapper
