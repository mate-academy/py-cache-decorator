from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def checker(*args: list[Any], **kwargs: dict[Any]) -> Any:
        request = str([*args, {**kwargs}])
        if request not in storage:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage.update({request: result})
            return result
        print("Getting from cache")
        return storage[request]

    return checker
