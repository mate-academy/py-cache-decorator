def cache(func):
    unique = {}

    def inner(*args):
        if args not in unique:
            unique[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return unique[args]

    return inner
