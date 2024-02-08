def union(*args) -> set:
    result_set = set()
    for s in args:
        if isinstance(s, (list, tuple, set)):
            result_set.update(s)
        else:
            raise TypeError("Input must be a list, tuple, or set.")
    return result_set


def intersect(*args) -> set:
    if not args:
        return set()

    # Initialize with the elements of the first set
    result_set = set(args[0])

    for s in args[1:]:
        if isinstance(s, (list, tuple, set)):
            result_set.intersection_update(s)
        else:
            raise TypeError("Input must be a list, tuple, or set.")

    return result_set


if __name__ == "__main__":
    assert union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']) == {'P', 'A', 'S', 'C', 'M'}
    assert intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')) == {'S', 'C'}
