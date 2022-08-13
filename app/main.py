def cache(func):
    runs_dict = {}

    def wrapper(*args, **kwargs):
        result = None
        if id(func) in runs_dict:
            for runs in runs_dict[id(func)]:
                if args == runs['args'] and kwargs == runs['kwargs']:
                    print('Getting from cache')
                    result = runs['result']
        else:
            print('Calculating new result')
            result = func(*args, **kwargs)
            runs_dict.update({id(func):
                             [{'args': args,
                               'kwargs': kwargs,
                               'result': result}]})
        if result is None:
            print('Calculating new result')
            result = func(*args, **kwargs)
            runs_dict[id(func)] += \
                [{'args': args,
                  'kwargs': kwargs,
                  'result': result}]
        return result

    return wrapper
