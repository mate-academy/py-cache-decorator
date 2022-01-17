def cache(func):
    hole = dict()

    def inner(*args):
        if args not in hole:
            hole[args] = func(*args)
            print('Calculating new result')
            return func
        if args in hole:
            print('Getting from cache')

            return hole[args]

    return inner
