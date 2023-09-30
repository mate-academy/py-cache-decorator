from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = {}
    immutable_type = (int, float, str, tuple, bool, type(None))

    def argument_based_cacher(*args) -> Any:
        nonlocal cached_data
        if all([isinstance(variable, immutable_type) for variable in args]):
            func_key = tuple(args)
            if func.__name__ not in cached_data.keys():
                cached_data[func.__name__] = {}
            if func_key in cached_data[func.__name__]:
                print("Getting from cache")
                return cached_data[func.__name__][func_key]
            print("Calculating new result")
            func_result = func(*args)
            cached_data[func.__name__][func_key] = func_result
            return func_result
        print("Calculating new result")
        return func(*args)
    return argument_based_cacher
