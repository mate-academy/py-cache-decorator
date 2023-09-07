from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    save_cache = {}

    def decorator(*args) -> Callable[..., Any]:

        if args not in save_cache:
            print("Calculating new result")
            result = func(*args)
            save_cache[args] = result
            return result
        else:
            print("Getting from cache")
            return save_cache[args]

    return decorator
