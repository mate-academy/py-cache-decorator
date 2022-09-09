
def cache(func):
    data = dict()

    def wrapper(*args, **kwargs):
        if args not in data:
            data[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return data[args]
    return wrapper
