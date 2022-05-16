def cache(func):
    result = {}

    def decorate(*args, **kwargs):
        if args in result:
            print('Getting from cache')
            return result[args]
        else:
            result[args] = func(*args, **kwargs)
            print('Calculating new result')
            return result[args]

    return decorate
