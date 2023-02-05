def cache(func):
    new_dict = {}

    def wrapper(*args):
        if args not in new_dict:
            new_dict[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return new_dict[args]
    return wrapper
