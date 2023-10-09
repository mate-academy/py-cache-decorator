from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(data: list) -> None:
        data_w_result = {}
        for elem in data:
            if elem in data_w_result:
                print("Getting from cache")
                print(data_w_result[elem])
            else:
                data_w_result.update({elem: func(data)})
    return inner


@cache
def long_time_func(data: list) -> None:
