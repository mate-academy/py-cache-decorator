from typing import Callable


def cache(func: Callable) -> Callable:
    database = []

    def inner(*args, **kwargs) -> Callable:
        in_cache = [
            data["result"] for data in database if data["arguments"] == args
        ]
        if in_cache:
            print("Getting from cache")
            return in_cache[0]
        print("Calculating new result")
        result = func(*args)
        database.append({"result": result, "arguments": args})
        return result

    return inner


@cache
def long_time_func(name_a: int, name_b: int, name_c: int) -> int:
    return (name_a ** name_b ** name_c) % (name_a * name_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
