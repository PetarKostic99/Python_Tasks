from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    result = []
    start = 0

    for index in indexes:
        if index <= len(s):
            result.append(s[start:index])
            start = index
    result.append(s[start:])

    return result


if __name__ == '__main__':
    assert (split_by_index('Ovo je probada seVidi', [2, 4, 12, 16])) == ['Ov', 'o ', 'je proba', 'da s', 'eVidi']
    assert (split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])) == ["python", "is", "cool", ",", "isn't",
                                                                             "it?"]
    assert (split_by_index("no luck", [42])) == ["no luck"]
