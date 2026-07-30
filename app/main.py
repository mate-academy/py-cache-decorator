from typing import Callable


def cache(func: Callable) -> Callable:
    cache_list = []

    def inner(*args) -> list:
        for element in cache_list:
            for key, value in element.items():
                if key == args:
                    print("Getting from cache")
                    return value
        print("Calculating new result")
        result = func(*args)
        cache_list.append({args: result})
        return result
    return inner


# @cache
# def long_time_func(a: int, b: int, c: int) -> int:
#     return (a ** b ** c) % (a * c)
#
# @cache
# def long_time_func_2(n_tuple: tuple, power: int) -> int:
#     return [number ** power for number in n_tuple]
#
# long_time_func(1, 2, 3)
# long_time_func(2, 2, 3)
# long_time_func_2((5, 6, 7), 5)
# long_time_func(1, 2, 3)
# long_time_func_2((5, 6, 7), 10)
# long_time_func_2((5, 6, 7), 10)
#
# # Calculating new result
# # Calculating new result
# # Calculating new result
# # Getting from cache
# # Calculating new result
# # Getting from cache
