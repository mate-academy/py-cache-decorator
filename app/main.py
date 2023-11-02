from typing import Callable, Any


data = []


def cache(func: Callable) -> Callable:
    def inner(*args: Any) -> Callable:
        for el in data:
            if el["args"] == args and el["func"] == func:
                print("Getting from cache")
                return el["result"]
        result = func(*args)
        print("Calculating new result")
        data.append({"args": args, "func": func, "result": result})
        return result

    return inner
