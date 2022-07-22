def cache(func):
    dictionary = {}

    def wrapper(*args):
        key = args
        if key not in dictionary.keys():
            print("Calculating new result")
            dictionary[key] = func(*args)
        else:
            print("Getting from cache")
        return dictionary[key]

    return wrapper
