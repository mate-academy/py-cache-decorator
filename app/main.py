def cache(func):
    cashed = dict()

    def wrapper(*args):
        if args not in cashed:
            print("Calculating new result")
            cashed[args] = func(*args)
        else:
            print("Getting from cache")
        return cashed[args]
    return wrapper
