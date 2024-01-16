from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    collection_all_func_with_result = []
    collection_all_func = []

    @wraps(func)
    def inner(*args) -> Callable:
        current_func = [func.__name__, args]

        if current_func in collection_all_func:
            print("Getting from cache")
            for i in collection_all_func_with_result:
                if i[0] == current_func[0] and i[1] == current_func[1]:
                    return i[2]
        else:
            print("Calculating new result")
            collection_all_func.append(current_func)
            result_func = func(*args)
            collection_all_func_with_result.append([func.__name__,
                                                    args, result_func])
            return result_func

    return inner

