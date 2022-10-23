def cache(func):
    cached_dict = {}
    def wrapper(*args):
        if args in cached_dict.keys():
            print("Getting from cache")
            return cached_dict[args]
        elif args not in cached_dict.keys():
            cached_dict[args] = func(*args)
            print("Calculating new result")
            return cached_dict[args]
        return func
    return wrapper

