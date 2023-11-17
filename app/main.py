from typing import Callable


def cache(func: Callable) -> Callable:
    cache_for_funk = {}
    cache_for_funk2 = {}

    def inner(*arg) -> Callable:
        if len(arg) == 3:
            a, b, c = arg
            if (a, b, c) in cache_for_funk:
                print("Getting from cache")
                result = cache_for_funk[(a, b, c)]
            else:
                print("Calculating new result")
                result = func(a, b, c)
                cache_for_funk[(a, b, c)] = result
            return result
        else:
            n_tuple, power = arg
            if (n_tuple, power) in cache_for_funk2:
                print("Getting from cache")
                result = cache_for_funk2[(n_tuple, power)]
            else:
                print("Calculating new result")
                result = func(n_tuple, power)
                cache_for_funk2[n_tuple, power] = result
            return result
    return inner
