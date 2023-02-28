from typing import Callable, Any


def cache(func: Callable) -> Any:
    collection_dict = {}

    def wrapper(*args: int) -> int:

        if args not in collection_dict:
            collection_dict[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return collection_dict[args]
    return wrapper
