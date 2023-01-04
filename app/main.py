from typing import Callable, Dict, Any, Hashable


def cache(func: Callable) -> Callable:
    cache_dict: Dict[Hashable, Hashable] = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[args] = func(*args, **kwargs)
        return cache_dict[args]

    return wrapper
