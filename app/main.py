import functools
from typing import Callable, Any


def cache(func: Callable) -> str:
    store = {}

    @functools.wraps(func)
    def inner(*args: Any) -> Any:
        if f"{func.__name__}" not in store.keys():
            store.update({f"{func.__name__}": {args: func(*args)}})
            print("Calculating new result")
        else:
            if args not in store[f"{func.__name__}"]:
                store[f"{func.__name__}"].update({args: func(*args)})
                print("Calculating new result")
            else:
                print("Getting from cache")
        return store[f"{func.__name__}"].get(args)

    return inner
