from typing import Callable, Any


def cache(func: Callable) -> Any:
    cache_for_func = {}

    def inner(*args: Any) -> int:
        key_cache = args
        if key_cache in cache_for_func:
            print("Getting from cache")
            result = cache_for_func[key_cache]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_for_func[key_cache] = result
        return result
    return inner
