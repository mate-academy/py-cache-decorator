def cache(func):
    cached_data = {}

    def inner(*args):
        if args not in cached_data:
            print("Calculating new result")
            cached_data[args] = func(*args)
            return cached_data[args]
        else:
            print("Getting from cache")
            return cached_data[args]
    return inner
