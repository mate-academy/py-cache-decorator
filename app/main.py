from typing import Callable


def cache(func: Callable) -> Callable:
    memory_cache = {}

    def inner(*args, **kwargs) -> list and int:
        cod_number = ""
        input_num = args[0] if type(args[0]) is tuple else args
        for each in input_num:
            cod_number += str(each) + "$"
        cod_number += str(args[1])

        if cod_number in memory_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            memory_cache[cod_number] = func(*args, **kwargs)
        return memory_cache[cod_number]

    return inner
