from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dic = dict()

    @wraps(func)
    def inner(*args, **kwargs) -> Any:

        key_cach = ", ".join([func.__name__, str(args), str(kwargs)])

        if key_cach in cache_dic:
            print("Getting from cache")
            return cache_dic[key_cach]

        cache_dic[key_cach] = func(*args, **kwargs)

        print("Calculating new result")
        return cache_dic[key_cach]

    return inner
