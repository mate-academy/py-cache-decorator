def cache(func):
    result_dict = {}

    def inner(*args):
        if args in result_dict:
            print('Getting from cache')
        else:
            print('Calculating new result')
            result_dict[args] = func(*args)
        return result_dict[args]
    return inner
