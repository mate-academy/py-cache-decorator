def cache(func):
    stored_values = {}

    def wrapper(*args):
        if args not in stored_values:
            print("Calculating new result")
            stored_values[args] = func(*args)
            return stored_values[args]
        else:
            print("Getting from cache")
            return stored_values[args]
    return wrapper
