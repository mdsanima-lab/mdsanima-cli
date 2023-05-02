# Copyritht © 2023 Marcin Różewski MDSANIMA


"""Tool timer measures the execution time for the decorated function we provide."""


from __future__ import annotations

import time
from functools import wraps


def timer(func):
    """This decorator returns the execution time in seconds for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        exec_time = round(end_time - start_time, 3)
        return exec_time

    return wrapper
