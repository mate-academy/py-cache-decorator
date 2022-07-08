def cache(func):
    saved = dict()

    def function(*args):
        key = str(args)
        if key not in saved.keys():
            val = func(*args)
            saved[key] = val
            print('Calculating new result')
            return val
        print('Getting from cache')
        return saved[key]
    return function
