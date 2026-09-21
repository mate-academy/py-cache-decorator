from typing import Callable


def cache(func: Callable) -> Callable:
    cache_buffer = []

    def inner(*args, **kwargs) -> any:
        for item in cache_buffer:
            if item["args"] == args:
                print("Getting from cache")
                return item["value"]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_buffer.append({"args": args, "value": result})
        return result
    return inner
