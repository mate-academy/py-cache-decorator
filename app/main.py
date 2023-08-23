from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    caching_result = {}
    wraps(func)

    def wrapper(*args: tuple) -> Any:
        nonlocal caching_result

        if func.__name__ not in caching_result.keys():
            print("Calculating new result")

            result = func(*args)

            caching_result[func.__name__] = [{
                "arguments": args,
                "result": result
            }]

            return result
        elif args not in [value["arguments"] for value in caching_result[func.__name__]]:
            print("Calculating new result")

            result = func(*args)

            caching_result[func.__name__].append({
                "arguments": args,
                "result": result
            })

            return result
        else:
            print("Getting from cache")

            for item in caching_result[func.__name__]:
                if item["arguments"] == args:
                    return item["result"]

    return wrapper


@cache
def long_time(*args):
    result = 1
    for i in args:
        result *= i
    return result


long_time(2, 2)
long_time(2, 2)
long_time(3, 2)
long_time(4, 2)
long_time(5, 2)
long_time(3, 2)
