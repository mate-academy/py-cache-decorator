def cache(func):
    c_dict = {}

    def inner(*args):
        if args in c_dict:
            print('Getting from cache')
            return c_dict[args]
        else:
            print('Calculating new result')
            c_dict[args] = func(*args)
            return c_dict[args]
    return inner
