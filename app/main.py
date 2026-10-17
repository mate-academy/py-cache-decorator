from typing import Any

def cache(func: Any) -> Any:
    _cached_storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in _cached_storage:
            print("Getting from cache")
            return _cached_storage[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            _cached_storage[cache_key] = result
            return result

    return wrapper
