from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # Check if the list has only one element
    if len(lst) <= 1:
        return []

    # Use a list comprehension to create pairs of elements
    pairs = [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]

    return pairs


if __name__ == "__main__":
    assert get_pairs([1, 2, 3, 8, 9]) == [(1, 2), (2, 3), (3, 8), (8, 9)]
    assert get_pairs(['need', 'to', 'sleep', 'more']) == [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
    assert get_pairs([1]) == []
