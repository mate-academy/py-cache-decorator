def cache(func):
    arguments = dict()

    def inner(*args):
        if args in arguments:
            print("Getting from cache")
            return arguments[args]
        else:
            print("Calculating new result")
            arguments[args] = func(*args)
            return func(*args)
    return inner
