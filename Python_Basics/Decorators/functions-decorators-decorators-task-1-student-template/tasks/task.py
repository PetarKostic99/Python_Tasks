from time import time, sleep
from typing import Dict

execution_time: Dict[str, float] = {}


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time[func.__name__] = end_time - start_time
        return result

    return wrapper


@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b


if __name__ == "__main__":
    result = func_add(10, 20)
    assert execution_time['func_add'] >= 0.2
