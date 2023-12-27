from typing import Callable, Any

def cache(func: Callable) -> Callable:
    cache_data = {}

    def inner(*args) -> Any:
        if not cache_data.get(func.__name__):
            result = func(*args)
            cache_data[func.__name__] = {}
            cache_data[func.__name__][args] = result
            print("Calculating new result")
            return result
        elif cache_data.get(func.__name__).get(args) is None:
            result = func(*args)
            cache_data[func.__name__][args] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return cache_data[func.__name__][args]
    return inner

#
# @cache
# def long_time_func(a, b, c):
#     return (a ** b ** c) % (a * c)
#
#
# @cache
# def long_time_func_2(text_1, text_2):
#     return f"{text_1.upper()}, {text_2.lower()}"
#
#
# @cache
# def long_time_func_3(n_list, text):
#     return f"{[i ** 2 for i in n_list]}, {text}"
#
# long_time_func(1, 2, 3)
# long_time_func(1, 2, 3)
# long_time_func(1, 2, 3)
# long_time_func_3((10, 20, 30), "wow, numbers!")
# long_time_func(2, 2, 3)
# long_time_func_2("Hello", "world")
# long_time_func(1, 2, 3)
# long_time_func_2("Hello", "Mark")
# long_time_func_2("Hello", "Mark")
# long_time_func_3((10, 20, 30), "wow, numbers!")
# long_time_func_3((10, 20, 30), "egh, numbers...")
#

