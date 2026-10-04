from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data_store = {}

    def check_cache(*args, **kwargs) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in data_store:
            print("Getting from cache")
            return data_store[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        data_store[cache_key] = result

        return result

    return check_cache
