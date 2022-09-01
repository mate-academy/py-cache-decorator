def cache(func):
    a = {}

    def wrapper(*args):
        if args in a:
            print('Getting from cache')
            return a[args]
        else:
            print('Calculating new result')
            a[args] = func(*args)
            return a[args]
    return wrapper
