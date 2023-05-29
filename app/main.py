from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_store = {}

    def wrapper(*args: Any) -> Any:
        if args not in result_store:
            print("Calculating new result")
            result_store[args] = func(*args)
        else:
            print("Getting from cache")

        return result_store.get(args)

    return wrapper
