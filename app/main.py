def cache(func: callable) -> callable:
    text_dicts = {}

    def inner(*args, **kwargs) -> dict:
        key = args
        if key not in text_dicts:
            print("Calculating new result")
            text_dicts[key] = func(*args, **kwargs)

        else:
            print("Getting from cache")
        return text_dicts[key]

    return inner
