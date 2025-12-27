from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = dict()

    def decorator(*data: Any) -> Any:
        if not len(data) == 1 and not isinstance(data[0], (list, set, dict)):
            if data in cache_data:
                print("Getting from cache")
                return cache_data[data]
            new_data = func(*data)
            cache_data[data] = new_data
            print("Calculating new result")
            return new_data

    return decorator
