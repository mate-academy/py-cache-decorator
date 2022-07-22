def cache(func):
    my_dictionary = {}

    def wrapper(*args):
        my_key = args
        if my_key not in my_dictionary.keys():
            print("Calculating new result")
            my_dictionary[my_key] = func(*args)
        else:
            print("Getting from cache")
        return my_dictionary[my_key]

    return wrapper
