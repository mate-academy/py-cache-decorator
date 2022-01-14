def cache(func):
    stored_results = {}

    def inner(*args):
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]
        else:
            print('Calculating new result')
            stored_results[args] = (result := func(*args))
            return result

    return inner
