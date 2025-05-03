from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> Any:
        args_key = args if isinstance(args, tuple) else (args,)
        kwargs_key = tuple(sorted(kwargs.items()))
        key = args_key + kwargs_key

        if key not in result:
            print("Calculating new result")
            result[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return result[key]

    return wrapper
