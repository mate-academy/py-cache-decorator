from typing import Callable, Any


def cache(func: Callable) -> Callable:
    input_and_result = {}

    def inner(*args) -> Any:
        if args in input_and_result:
            print("Getting from cache")
            return input_and_result[args]
        print("Calculating new result")
        func_result = func(*args)
        input_and_result.update({args: func_result})
        return func_result

    return inner
