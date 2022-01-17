def cache(func):
    storage = dict()

    def wrapper(*args):
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            storage[args] = func(*args)
            return func(*args)

    return wrapper
