from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Any:
        if args not in cache_dict.keys():
            cache_dict[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[args]

    return wrapper


@cache
def func_one(a, b):
    return a + b


@cache
def func_2(a, b):
    return a + b


func_one(1, 2)
func_2(2, 3)
func_one(1, 2)
func_2(2, 3)