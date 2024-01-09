from typing import List, Tuple, Union, Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args, **kwargs) -> Union[int, List[int], Tuple[int, int]]:
        key = (args, frozenset(kwargs.items()))
        if key in results_cache:
            print("Getting from cache")
            return results_cache[key]
        else:
            result = func(*args, **kwargs)
            results_cache[key] = result
            print("Calculating new result")
            return result

    return wrapper


@cache
def long_runtime_function(data: List[int]) -> List[int]:
    print(f"Running long runtime function with data: {data}")
    return [element * 2 for element in data]


@cache
def another_function(arg1: int, arg2: int) -> int:
    print(f"Running another function with arguments: {arg1}, {arg2}")
    return arg1 + arg2
