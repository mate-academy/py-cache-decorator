from typing import Callable, Any


def cache(func: Callable) -> Callable:
    global result_all
    result_all = []

    def inner(*args, **kqargs) -> Any:

        results = {"name": func, "arg": args}
        for result in result_all:
            if result["name"] == results["name"] \
                    and result["arg"] == results["arg"]:
                print("Getting from cache")
                return result["result"]

        print("Calculating new result")
        result_func = func(*args, **kqargs)
        results["result"] = result_func
        result_all.append(results)
        return result_func

    return inner
