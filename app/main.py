def cache(func):
    storage = {}

    def inner(*args):
        if args in storage.keys():
            print("Getting from cache")
        else:
            storage[args] = func(*args)
            print("Calculating new result")
        return storage[args]
    return inner
