from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stores = {}

    def inner(*args: Any) -> Any:
        if args in stores:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stores[args] = func(*args)

        return stores[args]

    return inner
