from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> None:
        cashe_key = (args, tuple(sorted(kwargs.items())))

        if cashe_key in results:
            print("Getting from cache")
            return results[cashe_key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        results[cashe_key] = result
        return result
    return wrapper
