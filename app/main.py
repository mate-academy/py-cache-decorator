from typing import Callable


def cache(func: Callable) -> Callable:

    result_history = {}
    input_history = []

    def wrapper(*args) -> Callable:
        arguments = ", ".join(str(arg) for arg in args)

        if arguments not in input_history:
            result = func(*args)
            input_history.append(arguments)
            result_history[arguments] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return result_history[arguments]
    return wrapper
