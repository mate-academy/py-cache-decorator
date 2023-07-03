from typing import Any


def cache(func) -> Any:
    data_save = {}

    def inner(*args: tuple[(int, float, tuple, str)]) -> Any:
        nonlocal data_save
        if args in data_save:
            print("Getting from cache")
            return data_save[args]
        else:
            print("Calculating new result")
            data_save[args] = func(*args)
            return data_save[args]
    return inner
