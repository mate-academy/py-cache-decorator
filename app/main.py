from typing import Callable, Any


def cache(func: Callable) -> Callable:
    previous_args = {}

    def inner(*args) -> Any:
        if all([
            isinstance(arg, (tuple, str, int, float, bool))
            for arg in args
        ]):
            if args in previous_args.keys():
                print("Getting from cache")
                return previous_args[args]
            else:
                func_result = func(*args)
                previous_args[args] = func_result
                print("Calculating new result")
                return func_result

    return inner
