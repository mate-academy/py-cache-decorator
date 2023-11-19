from typing import Callable


def cache(func: Callable) -> Callable:

    results = []

    def wrapper(*args) -> any:
        for result in results:
            if result["func"] == func and result["args"] == args:
                print("Getting from cache")
                return result["output"]

        print("Calculating new result")
        new_result = {"func": func, "args": args, "output": func(*args)}
        results.append(new_result)
        return new_result["output"]

    return wrapper
