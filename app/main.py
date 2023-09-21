from typing import Callable


def cache(func: Callable) -> Callable:
    results_list = []

    def inner(*args) -> Callable:
        nonlocal results_list
        for result in results_list:
            if result["arguments"] == [*args]:
                print("Getting from cache")
                return result["result_func"]
        results_list += [
            {
                "arguments": [*args],
                "result_func": func(*args)
            }
        ]
        print("Calculating new result")
        return results_list[-1].get("result_func")

    return inner
