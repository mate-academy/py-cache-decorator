from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def inner(*args) -> Any:
        items = args
        name_of_func = func.__name__
        if name_of_func in cache_storage \
                and items in cache_storage[name_of_func]:
            print("Getting from cache")
            return cache_storage[name_of_func][items]
        else:
            print("Calculating new result")
            result = func(*items)
            storage_update = {items: result}
            if name_of_func in cache_storage:
                cache_storage[name_of_func].update(storage_update)
            else:
                cache_storage.update({name_of_func: storage_update})
            return result
    return inner
