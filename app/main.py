from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(*args) -> int:

        for item in cash:
            if item[0] == func and item[1] == args:
                print("Getting from cache")
                return item[2]

        print("Calculating new result")
        result = func(*args)
        cash.append([func, args, result])
        return result

    return inner


cash = [[None, None, None]]
