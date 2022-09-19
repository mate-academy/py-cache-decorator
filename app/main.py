def cache(func):
    storage = {}

    def wrapper(*args):
        if args in storage:
            print("Getting from cache")

        else:
            storage.update({args: func(*args)})
            print("Calculating new result")

        return storage[args]

    return wrapper
