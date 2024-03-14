from typing import Callable


def cache(func: Callable) -> Callable:
    dic = {}

    def inner(*args, **kwargs) -> None:
        if args not in dic:
            dic.update({args: func(*args, **kwargs)})
            print("Calculating new result")
        else:
            print("Getting from cache")

        return dic[args]

    return inner
