from typing import Callable


def cache(func: Callable) -> Callable:
    memory_cache = {}

    def inner(*args, **kwargs) -> list and int:
        nonlocal memory_cache
        immute = (dict, set, list)
        for argumets in args:
            if type(argumets) in immute:
                return

        memory_cache_key = ""
        input_num = args[0] if type(args[0]) is tuple else args
        for each in input_num:
            memory_cache_key += str(each) + "$"
        memory_cache_key += str(args[1])

        if memory_cache_key in memory_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            memory_cache[memory_cache_key] = func(*args, **kwargs)
        return memory_cache[memory_cache_key]

    return inner
