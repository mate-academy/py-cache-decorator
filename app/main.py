def cache(func):
    dict_args_result = {}
    dict_name_func = {}

    def inner(*args, **kwargs):

        for key_name_func, value_name_func in dict_name_func.items():
            if key_name_func == str(func.__name__):
                for key_args_result, value_args_result in \
                        value_name_func.items():
                    if key_args_result == args:

                        print('Getting from cache')
                        return dict_args_result[args]

        dict_args_result[args] = func(*args, **kwargs)
        dict_name_func.update({func.__name__: dict_args_result})

        print('Calculating new result')
        return dict_args_result[args]

    return inner
