from typing import Callable
import time


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> float:
        if "cache_dic" not in globals():
            global cache_dic
            cache_dic = {}
        if func.__name__ in cache_dic:
            for elem in cache_dic[func.__name__]:
                for key, value in elem.items():
                    if key == str(args):
                        print("Getting from cache")
                        return value[1]

        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        result_time = round(end - start, 6)

        cache_dic.setdefault(func.__name__, [])
        cache_dic[func.__name__].append({str(args): [result_time, res]})

        print("Calculating new result")
        return res
    return inner


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


@cache
def long_time_func(num: int, num2: int, num3: int) -> int:
    return (num ** num2 ** num3) % (num * num3)


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
