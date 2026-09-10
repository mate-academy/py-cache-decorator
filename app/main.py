from typing import Callable


def cache(func: Callable) -> Callable:
    arr = []
    obj = {}

    def inner(*args) -> Callable:
        for item in arr:
            for key, value in item.items():
                if key == args:
                    print("Getting from cache")
                    return value

        res = func(*args)
        obj[args] = res
        print("Calculating new result")
        arr.append(obj)
        return res

    return inner


@cache
def long_time_func(num1: int, num2: int, num3: int) -> int:
    return num1 * num2 * num3
