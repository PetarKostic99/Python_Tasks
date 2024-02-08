from typing import Dict


def generate_squares(num: int) -> Dict[int, int]:
    # Asure that the number is positive
    if num < 0:
        num = abs(num)

    squares_dict = {i: i ** 2 for i in range(1, num + 1)}
    return squares_dict


if __name__ == "__main__":
    assert generate_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert generate_squares(-5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert generate_squares(0) == {}

