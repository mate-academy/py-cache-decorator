def cache(func):
    storage = {}

    def inner(*args):
        args = tuple(args)
        func_name = func.__name__

        if func_name in storage and args in storage[func_name]:
            print('Getting from cache')
            return storage[func_name][args]

        print('Calculating new result')
        func_res = func(*args)

        if func_name not in storage:
            storage[func_name] = {args: func_res}
        else:
            storage[func_name][args] = func_res
        return storage[func_name][args]

    return inner
