def cache(func):
    result = {}

    def wrapper(*args):
        if args in result:
            print("Getting from cache")
        else:
            result[args] = func(*args)
            print("Calculating new result")
        return result[args]

    return wrapper
