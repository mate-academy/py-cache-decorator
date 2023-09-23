from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def inner(*args) -> Any:
        if func not in cache_storage:
            cache_storage[func] = {}

        func_storage = cache_storage[func]
        if args not in func_storage:
            result = func(*args)
            func_storage.update({args: result})
            print("Calculating new result")
            return result
        print("Getting from cache")
        return func_storage[args]
    return inner
