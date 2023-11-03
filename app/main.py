from typing import Callable


def cache(func: Callable) -> Callable:
    cache = []

    def wrapper(*args) -> None:
        for data in cache:
            if data["arguments"] == args:
                print("Getting from cache")
                return data.get("result")

        results = func(*args)
        add_cache = {
            "arguments": args,
            "result": results
        }
        cache.append(add_cache)
        print("Calculating new result")

        return results

    return wrapper
