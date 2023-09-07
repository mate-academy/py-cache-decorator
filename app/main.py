from typing import Callable


def cache(func: Any) -> Any:
    save_cache = {}

    def decorator(*args: dict) -> Callable:

        if args not in save_cache:
            print("Calculating new result")
            result = func(*args)
            save_cache[args] = result
            return result
        else:
            print("Getting from cache")
            return save_cache[args]

    return decorator
