def cache(func):
    collection = {}
    def wrapper(*args, **kwargs):
        if args in collection:
            print("Getting from cache")
        else:
            collection[args] = func(*args)
            print("Calculating new result")
        return collection[args]
    return wrapper