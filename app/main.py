def cache(func):
    stored = {}

    def wrapper(*args):
        if args not in stored:
            stored[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return stored[args]
    return wrapper
