from typing import Callable


cash = []


def cache(func: Callable) -> Callable:
    def wrapper(*args) -> int:
        for item in cash:
            if item[0] == func and item[1] == args:
                print("Getting from cache")
                return item[2]
        else:
            print("Calculating new result")
            result = func(*args)
            cash.append([func, args, result])
            return result
    return wrapper
