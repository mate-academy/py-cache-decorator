cache_dict = {}


def cache(func):
    def inner(*args):
        global cache_dict
        if not cache_dict or func not in cache_dict:
            cache_dict.update({func: {args: func(*args)}})
            print("Calculating new result")
            return func(*args)
        else:
            if func in cache_dict and args not in cache_dict[func].keys():
                cache_dict[func][args] = func(*args)
                print("Calculating new result")
                return func(*args)
        print("Getting from cache")
        return cache_dict[func][args]
    return inner
