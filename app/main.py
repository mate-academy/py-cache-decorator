from typing import Callable


def cache(func: Callable) -> Callable:
    list_of_answers = {}

    def calc_or_cache(*args: tuple) -> dict:
        if args in list_of_answers.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            list_of_answers[args] = func(*args)
        return list_of_answers[args]
    return calc_or_cache
