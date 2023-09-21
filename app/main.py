from typing import Callable


def cache(func: Callable) -> Callable:
    results_dict = {}

    def inner(*args) -> Callable:
        nonlocal results_dict
        arguments = ", ".join(map(str, [*args]))
        if arguments in results_dict:
            print("Getting from cache")
            return results_dict[arguments]
        results_dict[arguments] = func(*args)
        print("Calculating new result")
        return results_dict[arguments]

    return inner
