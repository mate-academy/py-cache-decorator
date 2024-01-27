from typing import Callable


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args) -> Callable:
        name_func = func.__name__
        if name_func in result_dict:
            if args in [arg[0] for arg in result_dict[name_func]]:
                print("Getting from cache")
                result_num = [num for num in result_dict[name_func]
                              if num[0] == args][0][-1]
                return result_num
        print("Calculating new result")
        result_func = func(*args)
        result_dict[name_func] = (result_dict.get(name_func, [])
                                  + [[args] + [result_func]])
        return result_func
    return wrapper
