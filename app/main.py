def cache(func):
    info = {}

    def wrapper(*args):
        if args in info:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args)
            info[args] = result
        return info[args]
    return wrapper
