from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stores = {}

    def inner(*args: Any) -> Any:
        if args in stores:
            print("Getting from cache")
            return stores[args]
        stores[args] = func(*args)
        print("Calculating new result")
        return stores[args]

    return inner
