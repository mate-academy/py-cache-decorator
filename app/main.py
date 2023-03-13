from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_database = {}

    def wrapper(*args) -> Any:
        if tuple(args) not in cache_database:
            print("Calculating new result")
            cache_database[tuple(args)] = func(*args)
            return cache_database[tuple(args)]

        print("Getting from cache")
        return cache_database[tuple(args)]
    return wrapper
