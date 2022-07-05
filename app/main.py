def cache(func):
    list_arguments = {}

    def inner(*args):

        if args not in list_arguments:
            print('Calculating new result')
            list_arguments[args] = func(*args)

        else:
            print('Getting from cache')

        return list_arguments[args]

    return inner
