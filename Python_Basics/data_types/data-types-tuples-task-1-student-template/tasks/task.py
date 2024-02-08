from typing import Tuple


def get_tuple(num: int) -> str | tuple[int] | tuple[int, ...]:

    # Check if the input is an integer
    if not isinstance(num, int):
        return "Input is not an integer type"

    num = abs(num)

    # Base case: If the number is a single digit, return a tuple with that digit
    if num < 10:
        return (num,)

    # Use divmod to get the last digit and the remaining part of the number
    digit, remainder = divmod(num, 10)

    # Recursively call the function with the remaining part of the number
    # and concatenate the result with the last digit in a tuple
    return get_tuple(digit) + (remainder,)


if __name__ == "__main__":
    assert get_tuple(87178291199) == (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
    assert get_tuple(12345) == (1, 2, 3, 4, 5)
    assert get_tuple(-2653) == (2, 6, 5, 3)
    assert get_tuple(0) == (0,)
    assert get_tuple(21.365) == "Input is not an integer type"

