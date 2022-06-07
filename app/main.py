def cache(func):
    cached = {}

    def wrapper(*args):
        if args not in cached:
            cached[args] = func(*args)
            print("Calculating new result")
            return cached[args]
        else:
            print("Getting from cache")
            return cached[args]

    return wrapper
