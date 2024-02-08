from typing import List, Dict


def combine_dicts(*args: List[Dict[str, int]]) -> Dict[str, int]:
    """
    This function iterates over each dictionary passed as an argument,
    and for each key-value pair, it updates the result_dict by adding
    the values for identical keys or initializing them if the key is not present in the result dictionary.
    """
    result_dict = {}

    for d in args:
        for key, value in d.items():
            result_dict[key] = result_dict.get(key, 0) + value

    return result_dict


if __name__ == "__main__":
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    assert combine_dicts(dict_1, dict_2) == {'a': 300, 'b': 200, 'c': 300}
    assert combine_dicts(dict_1, dict_2, dict_3) == {'a': 600, 'b': 200, 'c': 300, 'd': 100}
