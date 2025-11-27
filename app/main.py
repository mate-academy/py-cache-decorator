from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        immutable_args = tuple(args)
        immutable_kwargs = tuple(sorted(kwargs.items()))
        cache_key = (immutable_args, immutable_kwargs)
        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
            return result

    return wrapper()
