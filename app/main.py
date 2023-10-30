from typing import Callable


def cache(func: Callable) -> Callable:
    # Write your code here
    cache_data = {}
    def inner(*arg, **kwarg) -> Callable:
        nonlocal cache_data

        print(arg)
        print(cache_data)
        if arg in list(cache_data.keys()):
            print(f"Getting from cache: {arg} result {cache_data[arg]}")
            print("Getting from cache")
            return cache_data[arg]
        else:
            cache_data[arg] = func(*arg, **kwarg)
            print("Calculating new result")
            return func(*arg, **kwarg)

        #     return cache_data[arg]
        # else:
        #     print("Calculating new result")
        return func(*arg, **kwarg)
    return inner


