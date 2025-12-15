from typing import Callable
import inspect


arg_cache = {}


def cache(func: Callable) -> Callable:

    def wrapper(*args) -> int:

        stack_name = inspect.stack()[1].function

        key = func.__name__

        if stack_name not in arg_cache:
            arg_cache[stack_name] = {}

        if key not in arg_cache[stack_name]:
            arg_cache[stack_name][key] = {}

        cache_tuple = args
        if (cache_tuple in arg_cache[stack_name][key]):
            print("Getting from cache")
        else:
            print("Calculating new result")
            arg_cache[stack_name][key][cache_tuple] = func(*args)
        return arg_cache[stack_name][key][cache_tuple]
    return wrapper
