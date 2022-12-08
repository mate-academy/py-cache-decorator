def cache(func):
    data = {}

    def wrapper(*args):
        if args not in data:
            print("Calculating new result")
            res = func(*args)
            data[args] = res
            return res
        else:
            print("Getting from cache")
            return data[args]

    return wrapper
