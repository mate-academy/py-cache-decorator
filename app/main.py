def cache(func):
    result = {}

    def caching(*args, **kwargs):

        if args in result.keys():
            print('Getting from cache')
            return result[args]
        else:
            result[args] = func(*args, **kwargs)
            print('Calculating new result')
            return result[args]

    return caching
