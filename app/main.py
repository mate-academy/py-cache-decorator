def cache(func):
    info = {}

    def wrapper(*args):
        nonlocal info
        if args in info:
            print('Getting from cache')
            for name, inf in info.items():
                if name == args:
                    return inf
        else:
            print('Calculating new result')
            result = func(*args)
            info[args] = result
            return result
    return wrapper
