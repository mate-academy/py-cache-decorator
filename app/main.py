from typing import Callable


def cache(func: Callable) -> Callable:
    items_dic = {}

    def wrapper(*args) -> int:
        nonlocal items_dic
        if args not in items_dic.keys():
            print("Calculating new result")
            res = func(*args)
            items_dic[args] = res
            return res
        else:
            print("Getting from cache")
            return items_dic.get(args)
    return wrapper
