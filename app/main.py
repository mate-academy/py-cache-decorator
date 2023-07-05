def cache(func: callable) -> callable:
    storage = {}

    def inner(*args) -> None:
        if args not in storage:
            res = func(*args)
            storage.update({args: res})
            print("Calculating new result")
            return res
        else:
            print("Getting from cache")
            return storage[args]

    return inner
