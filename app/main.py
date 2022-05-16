def cache(func):
    data = dict()

    def wrapper(*args):
        if args in data:
            print("Getting from cache")
            return data[args]
        else:
            result = func(*args)
            data[args] = result
            print("Calculating new result")
            return result

    return wrapper
