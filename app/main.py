def cache(func):
    result = {}

    def caching(*args, **kwargs):
        nonlocal result

        if f'{args}' in result.keys():
            print('Getting from cache')
        else:
            result[f'{args}'] = func(*args, **kwargs)
            print('Calculating new result')

    return caching
