import inspect
import logging
from collections import OrderedDict
from copy import deepcopy
from functools import wraps
from types import GeneratorType
from typing import Any, Callable

logger = logging.getLogger(__name__)


def cache(max_size: int | None = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        if inspect.iscoroutinefunction(func):
            raise TypeError("cache() does not support coroutine functions")

        if inspect.isgeneratorfunction(func):
            raise TypeError("cache() does not support generator functions")

        signature = inspect.signature(func)
        cache_storage: OrderedDict[
            tuple[tuple[Any, ...], tuple[tuple[str, Any], ...]],
            Any,
        ] = OrderedDict()

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()

            arguments = tuple(bound.arguments.values())
            key = (arguments, tuple(sorted(kwargs.items())))

            try:
                hash(key)
            except TypeError as error:
                raise TypeError(
                    "cache() supports only hashable arguments"
                ) from error

            if key in cache_storage:
                logger.debug("Getting from cache")
                result = cache_storage[key]

                if isinstance(result, (list, dict, set)):
                    return deepcopy(result)

                return result

            logger.debug("Calculating new result")
            result = func(*args, **kwargs)

            if isinstance(result, (list, dict, set)):
                cache_storage[key] = deepcopy(result)
            else:
                cache_storage[key] = result

            if max_size is not None:
                while len(cache_storage) > max_size:
                    cache_storage.popitem(last=False)

            return result

        def cache_clear() -> None:
            cache_storage.clear()

        wrapper.cache_clear = cache_clear
        return wrapper

    return decorator
