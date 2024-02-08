from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    total = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            total += seq_sum(element)  # Recursive call for nested sequences
        else:
            total += element
    return total


if __name__ == "__main__":
    assert seq_sum([1, (2, 3), 4, [[5, 6], 7], 8, 9]) == 45
    assert seq_sum([1, 2, 3, [4, 5, (6, 7)]]) == 28
    assert seq_sum([1, 2, 3, [4, 5, (6, 7)], -28]) == 0
