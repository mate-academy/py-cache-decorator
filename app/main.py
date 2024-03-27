from typing import Callable, Any


results = {}


def cache(func: Callable) -> Callable:
    def inner(*args: Any) -> Any:
        global results
        if (func, args) in results:
            print("Getting from cache")
            return results[(func, args)]
        else:
            print("Calculating new result")
            results[(func, args)] = (func(*args))
            return results[(func, args)]
    return inner
