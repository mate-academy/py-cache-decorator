from typing import Callable, Any


def cache(func: Callable) -> Callable:
    counter = 0
    args_counter = set()
    result_counter = dict()

    def wrapper(*args) -> Any:
        nonlocal counter
        counter += 1
        if args in args_counter:
            return func(*args)
        else:
            args_counter.add(args)
            result_counter[args] = func(*args)
            return func(*args)

    return wrapper

