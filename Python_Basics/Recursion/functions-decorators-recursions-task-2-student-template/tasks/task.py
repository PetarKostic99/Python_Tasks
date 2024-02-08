from typing import Any, List


def linear_seq(sequence: List[Any]) -> List[Any]:
    flattened_sequence = []
    for element in sequence:
        """ 
        This next condition is used to determine whether the current element 
        in the sequence is a nested sequence (either a list or a tuple). 
        """
        if isinstance(element, (list, tuple)):
            flattened_sequence.extend(linear_seq(element))  # Recursive call for nested sequences
        else:
            flattened_sequence.append(element)
    return flattened_sequence


if __name__ == "__main__":
    assert linear_seq([1, '2', '!', 2, 3, [3, [1, (7, [5, (2, 2), 65], 3), -5], 11], 8]) == [1, '2', '!', 2, 3, 3, 1, 7,
                                                                                             5, 2, 2, 65, 3, -5, 11, 8]
    assert linear_seq([1, 2, 3, [4, 5, (6, 7)]]) == [1, 2, 3, 4, 5, 6, 7]
