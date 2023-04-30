def cache(func):
    stored_results = {}
    def wrapper(*args):
        if args in stored_results:
            print('Getting from cache')
            return stored_results[args]
        else:
            print('Calculating new result')
            result = func(*args)
            stored_results[args] = result
            return result
    return wrapper