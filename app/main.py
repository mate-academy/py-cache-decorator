import logging
from functools import wraps
from typing import Any, Callable

logger = logging.getLogger(__name__)


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache_storage: dict[
        tuple[tuple[Any, ...], tuple[tuple[str, Any], ...]],
        Any,
    ] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        try:
            hash(key)
        except TypeError as error:
            raise TypeError(
                "cache() supports only hashable arguments"
            ) from error

        if key in cache_storage:
            logger.debug("Getting from cache")
            return cache_storage[key]

        logger.debug("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result

    return wrapper
