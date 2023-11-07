from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args) -> Any:
        if args in results:
            print("Getting from cache")
            return results[args]
        print("Calculating new result")
        temp_res = func(*args)
        results[args] = temp_res
        return temp_res

    return inner
