import functools


def cache(func):
    my_dict = {}

    @functools.wraps(func)
    def wrapper(*args):
        storage = (func, args)
        if storage in my_dict:
            print('Getting from cache')
            result = my_dict[storage]
        else:
            print('Calculating new result')
            result = func(*args)
            my_dict[storage] = result
        return result
    return wrapper
