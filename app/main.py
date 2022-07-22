def cache(func):
    dictionary = {}

    def wrapper(*args):
        if args not in dictionary.keys():
            print("Calculating new result")
            dictionary[args] = func(*args)
        else:
            print("Getting from cache")
        return dictionary[args]

    return wrapper
