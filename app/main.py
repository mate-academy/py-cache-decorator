def cache(func):
    dct_args_res = {}
    dct_name_fun = {}

    def inner(*args, **kwargs):

        for key_name_fun, val_name_fun in dct_name_fun.items():
            if key_name_fun == str(func.__name__):
                for key_args_res, value_args_res in val_name_fun.items():
                    if key_args_res == args:

                        print('Getting from cache')
                        return dct_args_res[args]

        dct_args_res[args] = func(*args, **kwargs)
        dct_name_fun.update({func.__name__: dct_args_res})

        print('Calculating new result')
        return dct_args_res[args]

    return inner
