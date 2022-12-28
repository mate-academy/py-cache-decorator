from typing import Callable


def store_data(func: Callable):
    result = {}
    result[func.__name__] = []
    def inner(num: int):
        if func(num) not in result[func.__name__]:
            result[func.__name__].append(func(num))
        else:
            print(f"Num is already in result")
        print(result)
    return inner



@store_data
def twice_number(num):
    return num * 2

@store_data
def trice_number(num):
    return num * 2

twice_number(50)
twice_number(100)
trice_number(2)
twice_number(50)
trice_number(2)
trice_number(5)


