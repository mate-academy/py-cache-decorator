def cache(func):
    storage = {}

    def inner(*args):
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            storage[args] = func(*args)
            print("Calculating new result")
            return storage[args]
    return inner
