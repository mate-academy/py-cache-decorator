def cache(func):
    runs_dict = {}

    def wrapper(*args):
        if args in runs_dict:
            print('Getting from cache')
        else:
            print('Calculating new result')
            runs_dict[args] = func(*args)
        return runs_dict[args]
    return wrapper
