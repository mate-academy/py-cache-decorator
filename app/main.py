from typing import Callable


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        immutable = True
        for arg in args:
            if (
                isinstance(arg, list)
                or isinstance(arg, dict)
                or isinstance(arg, set)
            ):
                immutable = False

        if not immutable:
            return func(*args, **kwargs)

        if args not in result_dict:
            print("Calculating new result")
            result_value = func(*args, **kwargs)
            result_dict[*args] = result_value
            return result_value
        else:
            print("Getting from cache")
            return result_dict[args]

    return wrapper
