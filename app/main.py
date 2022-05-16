import functools


def cache(func):
    memory = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in memory:
            print('Getting from cache')
            return memory[args]
        else:
            print("Calculating new result")
            cell = func(*args)
            memory[args] = cell
            return cell

    return wrapper


