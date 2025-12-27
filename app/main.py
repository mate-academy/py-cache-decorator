from typing import Callable, Dict, Any, Tuple, Hashable


def cache(func: Callable) -> Callable:

    cache_dict: Dict[Tuple[Hashable, ...], Any] = {}

    def wrapper(*args: Hashable, **kwargs: Hashable) -> Any:

        kwargs_tuple = tuple(sorted(kwargs.items()))

        cache_key = (args, kwargs_tuple)

        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)

        cache_dict[cache_key] = result

        return result

    return wrapper
