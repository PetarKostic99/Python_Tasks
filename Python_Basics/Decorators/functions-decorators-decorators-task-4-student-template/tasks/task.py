def decorator_apply(lambda_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = lambda_func(args[0])
            return func(result, *args[1:], **kwargs)

        return wrapper

    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    return num


if __name__ == "__main__":
    assert return_user_id(42) == 43
    assert return_user_id(2) == 3
