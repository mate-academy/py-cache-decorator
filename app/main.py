def cache(func):
    dictionary = {}

    def wrapper(*args):
        if args in dictionary.keys():
            print('Getting from cache')
            result = dictionary[args]
        else:
            result = func(*args)
            dictionary[args] = result
            print('Calculating new result')
        return result
    return wrapper
