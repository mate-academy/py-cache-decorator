from typing import Callable, Any

def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, frozenset(kwargs.items()))

        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        result = func(*args, **kwargs)
        cache_dict[cache_key] = result
        return result

    return wrapper
