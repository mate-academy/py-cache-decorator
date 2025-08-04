from typing import Callable


def cache(func: Callable) -> Callable:
    func_cache = []

    def inner(*args) -> int:
        cached_result = [res for res in func_cache if res["args"] == args]
        if cached_result:
            print("Getting from cache")
            return cached_result[0]["result"]
        else:
            result = func(*args)
            func_cache.append({
                "args": args,
                "result": result
            })
            print("Calculating new result")
            return result

    return inner
