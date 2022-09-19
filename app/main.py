def cache(func):
    container = {}

    def inner_function(*args):
        if args in container:
            print("Getting from cache")
            result_of_func = container[args]
        else:
            result_of_func = func(*args)
            container[args] = result_of_func
            print('Calculating new result')
        return result_of_func
    return inner_function
