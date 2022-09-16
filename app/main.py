def cache(func):
    store = {}

    def inner(*args):
        if args in store:
            print("Getting from cache")
        else:
            print("Calculating new result")
            store[args] = func(*args)

        return store[args]

    return inner
