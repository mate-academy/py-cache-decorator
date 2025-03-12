from typing import Callable, Any


def cache(func: Callable) -> Callable:
    """Cache decorator."""
    dict_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        # Użycie niemutowalnego klucza (tuple) dla cache
        cache_key = args

        if cache_key not in dict_cache:
            print("Calculating new result")
            result = func(*args, **kwargs)
            dict_cache[cache_key] = result
        else:
            print("Getting from cache")
        return dict_cache[cache_key]

    return wrapper
