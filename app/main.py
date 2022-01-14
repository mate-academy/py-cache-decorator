def cache(func):
    result_arr = []

    def inner(*args):
        tmp_args = []
        arr = [i for i in args]
        if arr in result_arr:
            print('Getting from cache')
            return func(*tuple(arr))
        else:
            for i in args:
                tmp_args.append(i)
            result_arr.append(tmp_args)
            print('Calculating new result')
            return func(*tuple(tmp_args))

    return inner
