from typing import Any, Callable


def cache(func: Callable) -> Callable:
    runs_data = {}

    def saver(*args) -> Any:
        if args in runs_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            runs_data[args] = func(*args)
        return runs_data[args]

    return saver
