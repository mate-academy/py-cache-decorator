from typing import Callable, Any


rezult_all = []


def cache(func: Callable) -> Callable:

    def inner(*args, **kqargs) -> Any:
        rezult = {"name": func, "arg": args}
        if len(rezult_all) < 1:
            rez_func = func(*args, **kqargs)
            print("Calculating new result")
            rezult["rezult"] = rez_func
            rezult_all.append(rezult)
            return rez_func

        for rez in rezult_all:
            if rez["name"] == rezult["name"] and rez["arg"] == rezult["arg"]:
                print("Getting from cache")
                return rez["rezult"]

        print("Calculating new result")
        rez_func = func(*args, **kqargs)
        rezult["rezult"] = rez_func
        rezult_all.append(rezult)
        return rez_func

    return inner
