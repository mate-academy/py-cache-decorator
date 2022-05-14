def cache(func):
    result = {}

    def decorate(*args, **kwargs):
        nonlocal result
        if args in result:
            print('Getting from cache')
            return result[args]
        else:
            result[args] = func(*args, **kwargs)
            print('Calculating new result')
            return func(*args, **kwargs)

    return decorate
