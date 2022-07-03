def cache(func):
    list_arguments = []

    def inner(*args):

        if args not in list_arguments:
            list_arguments.append(args)
            print('Calculating new result')
            global result
            result = func(*args)

        else:
            print('Getting from cache')

        return result

    return inner
