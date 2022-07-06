def cache(func):
    dict_arguments = {}

    def inner(*args):

        if args not in dict_arguments:
            print('Calculating new result')
            dict_arguments[args] = func(*args)

        else:
            print('Getting from cache')

        return dict_arguments[args]

    return inner
