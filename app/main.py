from typing import Callable


def cache(func):
    storage = {}  # um dicionário só
    
    def wrapper(*args):
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            result = func(*args)  # chama a função original
            storage[args] = result
            print("Calculating new result")
            return result
    
    return wrapper