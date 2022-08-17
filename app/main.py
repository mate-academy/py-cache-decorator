def cache(func):
    storage = {}

    def wrapper(*args):
        nonlocal storage
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            storage[args] = func(*args)
            return storage[args]
    return wrapper
