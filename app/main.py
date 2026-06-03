from typing import Callable, Any


def cache(func: Callable) -> Callable:
    main_cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if args in main_cache.keys():
            print("Getting from cache")
        else:
            main_cache[args] = func(*args, **kwargs)
            print("Calculating new result")
        return main_cache[args]
    return wrapper
