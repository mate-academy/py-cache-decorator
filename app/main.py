from functools import wraps


def cache(func: callable) -> callable:
    storage = {}

    @wraps(func)
    def inner(*args) -> None:
        if args not in storage:
            res = func(*args)
            storage.update({args: res})
            print("Calculating new result")
            return res

        print("Getting from cache")
        return storage[args]

    return inner
