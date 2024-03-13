from typing import Callable


def cache(func: Callable) -> Callable:
    used_args = set()
    cached_res = {}

    def inner(*args) -> Callable:
        for call in used_args:
            if args == call:
                print("Getting from cache")
                return cached_res[id(call)]
        used_args.add(args)
        cached_res[id(args)] = func(*args)
        print("Calculating new result")
        return cached_res[id(args)]
    return inner


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(text_1, text_2):
    return f"{text_1.upper()}, {text_2.lower()}"


@cache
def long_time_func_3(n_list, text):
    return f"{[i ** 2 for i in n_list]}, {text}"


@cache
def empty_func() -> None:
    return "XXX"


print(long_time_func(1, 2, 3))
print(long_time_func(1, 2, -100))
print(long_time_func(1, 2, 3))
print(long_time_func_2("Hello", "Mark"))
print(long_time_func_2("Hello", "Mark"))
print(long_time_func_3((10, 20, 30), "wow, numbers!"))
print(long_time_func_3((10, 20, 30), "egh, numbers..."))
print(long_time_func_2("Hello", "SMark"))
print(long_time_func_2("Hello", "Mark"))
print(long_time_func_2("Hello", "Mark"))
print(long_time_func_2("Hello", "Mark"))
print(long_time_func_2("Hello", "Mark"))
print(long_time_func_2("Hello", "SMark"))
print(empty_func())
print(empty_func())
