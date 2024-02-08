from typing import Union

NumType = Union[int, float]


def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
    result = None
    # add your code here
    result = (12 * a + 25 * b) / (1 + a ** (2 ** b))
    return round(result,  2)


if __name__ == "__main__":
    assert some_expression_with_rounding(3, 3) == 0.02
    assert some_expression_with_rounding(0, 0) == 0
    assert some_expression_with_rounding(1, 3.3) == 47.25
    assert some_expression_with_rounding(2, 3) == 0.39

