def cache(func):
    save = {}

    def wrapper(*args):
        if args in save:
            print("Getting from cache")
            return save[args]
        result = func(*args)
        save[args] = result
        print("Calculating new result")
        return result

    return wrapper
