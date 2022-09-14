def cache(func):
    dictionary = {}

    def wrapper(*args):
        if args in dictionary.keys():
            print('Getting from cache')
            return dictionary[args]
        else:
            res = func(*args)
            dictionary[args] = res
            print('Calculating new result')
            return res

    return wrapper
