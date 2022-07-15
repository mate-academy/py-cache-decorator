def cache(func):

    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Getting from cache")
        else:
            cache[args] = func(*args)
            print("Calculating new result")
        return cache[args]
    return wrapper
