def cache(func):
    cached = {}

    def wrapper(*args):
        if args not in cached:
            cached[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached[args]

    return wrapper
