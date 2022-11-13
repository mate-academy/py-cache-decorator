import functools


def cache(func):

    repository = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in repository:
            result = func(*args)
            repository.update({args: result})
            print("Calculating new result")
        else:
            print("Getting from cache")
        return repository[args]
    return wrapper
