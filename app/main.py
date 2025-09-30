from functools import wraps
from typing import Any, Callable, Hashable


def make_hashable(obj: Any) -> Hashable:
    """
    Converte objetos mutáveis em equivalentes hashable.
    Ex.: list -> tuple, dict -> tuple ordenada, set -> frozenset.
    """
    try:
        hash(obj)
        return obj
    except TypeError:
        if isinstance(obj, (list, tuple)):
            return tuple(make_hashable(item) for item in obj)
        if isinstance(obj, dict):
            return tuple(sorted((key, make_hashable(value))
                                for key, value in obj.items()))
        if isinstance(obj, set):
            return frozenset(make_hashable(item) for item in obj)
        raise TypeError(f"Tipo não hashable: {type(obj)}")


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator que guarda resultados já calculados.
    - Se os argumentos já foram usados antes → retorna do cache.
    - Caso contrário → executa a função, guarda no cache e retorna.
    """
    cache_store = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (make_hashable(args), make_hashable(kwargs))
        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_store[key] = result
        return result

    return wrapper
