def cache(func):
    storage = {}

    def wrapper(*args):
        if storage.get(args) is not None:
            print("Getting from cache")
            return storage.get(args)
        temp = func(*args)
        storage.update({args: temp})
        print("Calculating new result")
        return storage.get(args)
    return wrapper
