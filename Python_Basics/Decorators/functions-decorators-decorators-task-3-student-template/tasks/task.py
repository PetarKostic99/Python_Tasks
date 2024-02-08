from functools import wraps


def validate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Validate function arguments.

        Checks if all arguments are within the valid range (0 to 256, inclusive).

        Parameters:
        - *args: Variable-length argument list.
        - **kwargs: Arbitrary keyword arguments.

        Returns:
        - str: Message indicating success or failure.
        """
        if not all(0 <= arg <= 256 for arg in args):
            return "Function call is not valid!"
        else:
            return "Pixel created!"

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    """
    Create a pixel with RGB values.

    Returns:
    - str: Message indicating success or failure.
    """
    if 0 <= x <= 256 and 0 <= y <= 256 and 0 <= z <= 256:
        return "Pixel created!"
    else:
        return "Function call is not valid!"


if __name__ == "__main__":
    assert set_pixel(0, 127, 300) == "Function call is not valid!"
    assert set_pixel(0, 127, 250) == "Pixel created!"
