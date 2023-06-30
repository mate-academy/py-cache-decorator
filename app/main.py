from typing import Callable


def cache(func: Callable) -> Callable:
    cach = {}

    def wrapper(*args: None) -> None:
        if args in cach:
            print("Getting from cache")
            # print(cach[args])
            return cach[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cach[args] = result
            # print(result)
            return result
    return wrapper
