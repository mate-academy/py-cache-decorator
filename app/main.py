def cache(func):
    storage = dict()

    def wrapper(*args):
        if args in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args)

        return storage[args]

    return wrapper
