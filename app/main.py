from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def wrapper(*args) -> Callable:
        if f"Result with arguments{args}" in memory:

            print("Getting from cache")
            return memory[f"Result with arguments{args}"]

        else:
            result_of_function = func(*args)
            memory[f"Result with arguments{args}"] = result_of_function
            print("Calculating new result")
            return result_of_function

    return wrapper
