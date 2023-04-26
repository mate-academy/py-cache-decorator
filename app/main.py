from typing import Callable, Any


def cache(func: Callable) -> Callable:
    args_cache = {}

    def saved_result(*args: Any) -> Any:
        nonlocal args_cache
        args_new = tuple(args)
        if args_new in args_cache.keys():
            print("Getting from cache")
        else:
            args_cache[args_new] = func(*args)
            print("Calculating new result")
        return args_cache[args_new]
    return saved_result
