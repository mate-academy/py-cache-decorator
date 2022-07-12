def cache(func):
    save = {}

    def wrapper(*args):
        if args not in save:
            result = func(*args)
            save[args] = result
            print("Calculating new result")
            return result
        print("Getting from cache")
        return save[args]

    return wrapper
