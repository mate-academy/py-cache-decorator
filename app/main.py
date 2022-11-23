def cache(func):
    storage = {}

    def wrapper(*args):

        if args in storage.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args)
        print(storage[args])
        return storage[args]

    return wrapper
