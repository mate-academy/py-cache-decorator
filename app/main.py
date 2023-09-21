from typing import Callable

results_list = []


def cache(func: Callable) -> Callable:
    def inner(*args) -> Callable:
        global results_list
        for result in results_list:
            if (result["arguments"] == [*args]
                    and result["id_func"] == id(func)):
                print("Getting from cache")
                return result["result_func"]
        results_list += [
            {
                "arguments": [*args],
                "result_func": func(*args),
                "id_func": id(func)
            }
        ]
        print("Calculating new result")
        return results_list[-1].get("result_func")
    return inner
