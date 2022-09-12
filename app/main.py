def cache(func):
    storage = {}

    def wrapper(*args):
        if args in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args)
        return storage[args]
    return wrapper
