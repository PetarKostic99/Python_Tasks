from typing import Any, Dict, List, Set


def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    unique_set = set()

    for dictionary in lst:
        for value in dictionary.values():
            unique_set.add(value)

    return unique_set


if __name__ == "__main__":
    assert check([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                  {"VIII": "S007"}]) == {'S009', 'S005', 'S007', 'S001', 'S002'}
    assert check(
        [{"A": "RGB"}, {"B": "KTP"}, {"A": "UDP"}, {"B": "SST"}, {"S": "KTP"}, {"B": "UDP"}, {"S": "CCY"}]) == {'RGB',
                                                                                                                'CCY',
                                                                                                                'UDP',
                                                                                                                'KTP',
                                                                                                                'SST'}
    assert check([{"V": "1"}, {"V": "2"}, {"VI": "3"}, {"VI": "2"}, {"VII": "3"}, {"V": "1"}, {"VIII": "4"}]) == {'1',
                                                                                                                  '3',
                                                                                                                  '2',
                                                                                                                  '4'}
