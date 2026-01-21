from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> Any:

        cache_code = str(args)

        if cache_code not in cache_dict:
            result = func(*args, **kwargs)
            cache_dict[cache_code] = result
            print("Calculating new result")
        else:
            result = cache_dict[cache_code]
            print("Getting from cache")
        return result

    return inner
