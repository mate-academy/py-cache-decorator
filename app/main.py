from typing import Callable, Any

my_own_cache = {}


def cache(func: Callable) -> Callable:

    def validate(*args, **kwargs) -> Any:
        if func not in my_own_cache:
            my_own_cache[func] = {}
        if args not in my_own_cache[func]:
            print("Calculating new result")
            my_own_cache[func][args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return my_own_cache[func][args]

    return validate
