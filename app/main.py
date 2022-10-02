import functools
import json


def cache(func):
    saved_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if func.__name__ in saved_results:
            if str(args) in saved_results[func.__name__]:
                print("Getting from cache")
                return saved_results[func.__name__][str(args)]
            else:
                print("Calculating new result")
                saved_results[func.__name__].\
                    update({str(args): func(*args, **kwargs)})
                with open("data.json", "w") as f:
                    json.dump(saved_results, f)
                return saved_results[func.__name__][str(args)]
        else:
            print("Calculating new result")
            saved_results[func.__name__] = {str(args): func(*args, **kwargs)}
            with open("data.json", "w") as f:
                json.dump(saved_results, f)
            return saved_results[func.__name__][str(args)]

    return wrapper
