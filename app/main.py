import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        # 2. Tworzenie klucza: Łączymy args i kwargs w niemutowalną krotkę
        cache_key = (args, tuple(sorted(kwargs.items())))

        # 3. Sprawdzenie Cache'u
        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]

        # 4. Obliczanie i Zapis
        else:
            print("Calculating new result")
            # Wywołujemy faktyczne, długie obliczenia
            result = func(*args, **kwargs)

            # Zapisujemy wynik przed zwróceniem
            cache_dict[cache_key] = result
            return result

    return wrapper
